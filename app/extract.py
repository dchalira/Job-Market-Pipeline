import requests
import pandas as pd
import logging
from typing import Optional

logger = logging.getLogger(__name__)

API_URL = "https://remoteok.com/api"
REQUEST_TIMEOUT = 30
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; JobMarketPipeline/1.0)"
}


def fetch_jobs() -> pd.DataFrame:
    """
    Fetch job listings from the RemoteOK public API.

    Returns:
        pd.DataFrame: Raw job postings. Empty DataFrame on failure.
    """
    logger.info("Fetching jobs from RemoteOK API...")

    try:
        response = requests.get(API_URL, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            logger.error("Unexpected API response format: expected a list.")
            return pd.DataFrame()

        # First item is metadata — filter to valid job dicts only
        jobs = [
            job for job in data
            if isinstance(job, dict) and "position" in job
        ]

        if not jobs:
            logger.warning("No valid job records found in API response.")
            return pd.DataFrame()

        df = pd.DataFrame(jobs)

        # ── Build job_url from slug field ─────────────────────────────────────
        # RemoteOK API returns a 'slug' field e.g. "remote-python-dev-at-acme-123"
        # Full job URL pattern: https://remoteok.com/remote-jobs/{slug}
        if "url" in df.columns:
            df["job_url"] = df["url"].apply(
                lambda u: f"https://remoteok.com{u}" if isinstance(u, str) and u.startswith("/") else u
            )
        elif "slug" in df.columns:
            df["job_url"] = "https://remoteok.com/remote-jobs/" + df["slug"].astype(str)
        else:
            logger.warning("No 'url' or 'slug' field found in API response — job_url will be null.")
            df["job_url"] = None

        logger.info(f"Fetched {len(df)} job records.")
        return df

    except requests.exceptions.Timeout:
        logger.error(f"Request timed out after {REQUEST_TIMEOUT}s.")
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error: {e.response.status_code} - {e.response.reason}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error while fetching jobs: {e}")
    except ValueError as e:
        logger.error(f"Failed to parse JSON response: {e}")

    return pd.DataFrame()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    df = fetch_jobs()
    print(df[["position", "company", "job_url"]].head())