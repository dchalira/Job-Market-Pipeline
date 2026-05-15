import logging
import sys

from app.extract import fetch_jobs
from app.transform import transform_jobs
from app.load import create_schema, load_jobs

# ── Logging Setup ─────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("pipeline.log", encoding="utf-8"),
    ],
)

logger = logging.getLogger(__name__)


def run_pipeline() -> None:
    """
    Orchestrate the full ETL pipeline:
        1. Extract  — fetch raw jobs from RemoteOK API
        2. Transform — clean, normalize, and enrich the data
        3. Load      — persist to PostgreSQL database
    """
    logger.info("=" * 55)
    logger.info("  Job Market ETL Pipeline — Starting")
    logger.info("=" * 55)

    # ── Extract ───────────────────────────────────────────────
    logger.info("[1/3] Extract: Fetching raw job data...")
    raw_df = fetch_jobs()

    if raw_df.empty:
        logger.error("Extract stage returned no data. Aborting pipeline.")
        sys.exit(1)

    # ── Transform ─────────────────────────────────────────────
    logger.info("[2/3] Transform: Cleaning and normalizing data...")
    clean_df = transform_jobs(raw_df)

    if clean_df.empty:
        logger.error("Transform stage returned no data. Aborting pipeline.")
        sys.exit(1)

    # ── Load ──────────────────────────────────────────────────
    logger.info("[3/3] Load: Writing data to PostgreSQL...")
    create_schema()
    load_jobs(clean_df)

    logger.info("=" * 55)
    logger.info("  Pipeline completed successfully ✓")
    logger.info("=" * 55)


if __name__ == "__main__":
    run_pipeline()