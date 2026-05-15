import logging
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from config.config import DATABASE_URL

logger = logging.getLogger(__name__)

TABLE_NAME = "job_postings"
SCHEMA_PATH = Path(__file__).resolve().parent.parent / "db" / "schema.sql"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def create_schema() -> None:
    """
    Execute the SQL schema file to initialize database tables.

    Raises:
        FileNotFoundError: If schema.sql does not exist.
        SQLAlchemyError: If schema execution fails.
    """
    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(f"Schema file not found: {SCHEMA_PATH}")

    logger.info(f"Applying schema from {SCHEMA_PATH}...")

    try:
        with engine.begin() as conn:
            schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
            conn.execute(text(schema_sql))
        logger.info("Schema applied successfully.")

    except SQLAlchemyError as e:
        logger.error(f"Failed to apply schema: {e}")
        raise


def load_jobs(df: pd.DataFrame) -> None:
    """
    Load transformed job postings into the PostgreSQL database.

    Args:
        df: Cleaned DataFrame from transform stage.

    Raises:
        SQLAlchemyError: If the database insert fails.
    """
    if df.empty:
        logger.warning("No data to load — skipping database insert.")
        return

    logger.info(f"Loading {len(df)} records into '{TABLE_NAME}'...")

    try:
        df.to_sql(
            TABLE_NAME,
            engine,
            if_exists="append",
            index=False,
            method="multi",
            chunksize=500,       # Avoids memory issues on large payloads
        )
        logger.info(f"Successfully loaded {len(df)} rows into '{TABLE_NAME}'.")

    except SQLAlchemyError as e:
        logger.error(f"Database load failed: {e}")
        raise