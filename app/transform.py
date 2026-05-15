import pandas as pd
import logging

logger = logging.getLogger(__name__)

REQUIRED_COLUMNS = [
    "company",
    "position",
    "location",
    "salary_min",
    "salary_max",
    "tags",
    "date",
    "job_url",       # ← added
]

COLUMN_RENAMES = {
    "tags": "skills",
    "date": "posted_date",
}


def _normalize_tags(value) -> str:
    """Convert tag lists or raw values to a comma-separated string."""
    if isinstance(value, list):
        return ", ".join(str(t) for t in value)
    return str(value) if pd.notna(value) else ""


def _normalize_salary(df: pd.DataFrame) -> pd.DataFrame:
    """Coerce salary columns to numeric, replacing invalid entries with NaN."""
    for col in ("salary_min", "salary_max"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def _normalize_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Parse posted_date to datetime if column exists."""
    if "posted_date" in df.columns:
        df["posted_date"] = pd.to_datetime(df["posted_date"], errors="coerce")
    return df


def _normalize_urls(df: pd.DataFrame) -> pd.DataFrame:
    """Validate job_url entries — nullify malformed URLs."""
    if "job_url" in df.columns:
        df["job_url"] = df["job_url"].apply(
            lambda u: u if isinstance(u, str) and u.startswith("http") else None
        )
    return df


def transform_jobs(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform raw job postings into a structured format.

    Steps:
        - Selects only relevant columns (including job_url)
        - Normalizes tags/skills to comma-separated strings
        - Coerces salary fields to numeric
        - Parses dates to datetime
        - Validates job URLs
        - Removes duplicates
        - Adds source metadata column

    Args:
        df: Raw DataFrame from extract stage.

    Returns:
        pd.DataFrame: Cleaned and transformed job postings.
    """
    if df.empty:
        logger.warning("Received empty DataFrame — skipping transform.")
        return df

    # Keep only available columns from the desired set
    available_columns = [c for c in REQUIRED_COLUMNS if c in df.columns]
    missing = set(REQUIRED_COLUMNS) - set(available_columns)
    if missing:
        logger.warning(f"Missing expected columns: {missing}")

    df = df[available_columns].copy()

    # Normalize tags → skills
    if "tags" in df.columns:
        df["tags"] = df["tags"].apply(_normalize_tags)

    # Rename columns
    df.rename(columns=COLUMN_RENAMES, inplace=True)

    # Normalize types
    df = _normalize_salary(df)
    df = _normalize_dates(df)
    df = _normalize_urls(df)       # ← added

    # Strip whitespace from string columns
    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())

    # Add source metadata
    df["source"] = "RemoteOK"

    # Deduplicate
    before = len(df)
    df = df.drop_duplicates()
    dropped = before - len(df)
    if dropped:
        logger.info(f"Removed {dropped} duplicate rows.")

    logger.info(f"Transform complete: {len(df)} clean records.")
    return df