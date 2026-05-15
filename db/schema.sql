CREATE TABLE IF NOT EXISTS job_postings (
    id SERIAL PRIMARY KEY,
    company TEXT,
    position TEXT,
    location TEXT,
    salary_min NUMERIC,
    salary_max NUMERIC,
    skills TEXT,
    posted_date TIMESTAMP, -- Changed from DATE to keep the time
    job_url TEXT,
    source TEXT,
    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);