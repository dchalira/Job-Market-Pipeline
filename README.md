## Job Market Data Pipeline
## End-to-End Web Scraping + Data Engineering Project

This project demonstrates a complete modern data engineering workflow using Python, PostgreSQL, Docker, automated scheduling, CI/CD, and Power BI-ready analytics.

The pipeline collects job postings from the RemoteOK API, transforms the data, stores it in PostgreSQL, and prepares analytics-ready datasets for reporting and visualization.

Project Objectives

This project was built to demonstrate practical skills in:

* Web scraping and API ingestion
* ETL pipeline development
* Data transformation using pandas
* PostgreSQL database integration
* Docker containerization
* GitHub CI/CD automation
* Workflow scheduling
* Data analytics engineering
* Power BI integration
* Data Source

Source: RemoteOK API

API Endpoint:

https://remoteok.com/api

The pipeline extracts:

Job title
Company
Location
Salary ranges
Skills/tags
Job posting date
Direct job link

## Pipeline Architecture

RemoteOK API
      ↓
Extract Layer (Python Requests)
      ↓
Transform Layer (pandas)
      ↓
PostgreSQL Database
      ↓
Automation Scripts (.bat / .sh)
      ↓
Docker Containers
      ↓
GitHub CI/CD
      ↓
Power BI Dashboard

## Project Structure
Job-Market-Pipeline/
│
├── app/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── main.py
│   └── utils.py
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── db/
│   └── schema.sql
│
├── tests/
│   ├── __init__.py
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── logs/
│   └── pipeline.log
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .env
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── run_pipeline.bat
├── run_pipeline.sh
└── README.md

## Technologies Used
Layer	Technology
Language	Python
Data Processing	pandas
API Requests	requests
Database	PostgreSQL
ORM	SQLAlchemy
Containerization	Docker
Orchestration	Docker Compose
Testing	pytest
CI/CD	GitHub Actions
Visualization	Power BI
IDE	VS Code
Features
Extracts latest job postings from RemoteOK API
Loads up to 150 latest jobs per execution
Daily pipeline automation
PostgreSQL database integration
Duplicate prevention using unique job URLs
Dockerized ETL pipeline
Automated testing with pytest
CI/CD with GitHub Actions
Power BI-ready schema
Logging and monitoring support
Database Schema
CREATE TABLE IF NOT EXISTS job_postings (
    id SERIAL PRIMARY KEY,
    company TEXT,
    position TEXT,
    location TEXT,
    salary_min FLOAT,
    salary_max FLOAT,
    skills TEXT,
    posted_date DATE,
    job_url TEXT UNIQUE,
    source TEXT,
    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Setup Instructions
1. Clone Repository
git clone https://github.com/YOUR_USERNAME/job-market-pipeline.git

cd job-market-pipeline
2. Create Virtual Environment
PowerShell
python -m venv .venv

.venv\Scripts\Activate.ps1
Git Bash
python -m venv .venv

source .venv/Scripts/activate
3. Install Dependencies
pip install -r requirements.txt
Environment Variables

Create a .env file in project root.

DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=job_market
DB_USER=postgres
DB_PASSWORD=yourpassword
Running the Pipeline
Run manually
python -m app.main
Automated Execution
Windows
.\run_pipeline.bat
Git Bash / Linux
./run_pipeline.sh

The pipeline can also be scheduled daily using:

Windows Task Scheduler
cron jobs
Docker scheduling
Apache Airflow (future improvement)
Running Tests
pytest
Docker Setup
Build containers
docker-compose build
Run containers
docker-compose up
PostgreSQL Verification

Connect using pgAdmin or psql.

Example query:

SELECT COUNT(*) AS total_jobs
FROM job_postings;
Power BI Integration

Inside Power BI:

Get Data → PostgreSQL

Use:

Setting	Value
Server	localhost
Port	5432
Database	job_market
Suggested Dashboard Analytics
Top hiring companies
Most requested skills
Salary distributions
Jobs by location
Daily job trends
Remote work trends
GitHub CI/CD

GitHub Actions automatically:

installs dependencies
runs tests
validates pipeline integrity

Workflow file:

.github/workflows/ci.yml
Logging

Pipeline execution logs are stored in:

logs/pipeline.log
Future Improvements

## Potential enhancements:

Apache Airflow orchestration
Kafka streaming ingestion
AWS deployment
dbt transformations
Streamlit dashboard
FastAPI endpoints
Data quality validation
Historical trend analysis

## Portfolio Value

This project demonstrates practical skills in:

ETL pipeline development
Data engineering
API integration
PostgreSQL database management
Docker containerization
CI/CD engineering
Analytics engineering
BI dashboard integration

Suitable for roles such as:

Data Analyst
Data Engineer
Analytics Engineer
BI Developer
Junior DataOps / DevOps Engineer

## Author

Davie Denson Chalira

End-to-End Data Engineering Portfolio Project