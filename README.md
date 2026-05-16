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

## The pipeline extracts:

* Job title
* Company
* Location
* Salary ranges
* Skills/tags
* Job posting date
* Direct job link

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

## 📂 Project Structure

```text
Job-Market-Pipeline/
├── .github/
│   └── workflows/
│       └── ci.yml             # CI/CD pipeline configuration
├── app/                       # Main Application Logic
│   ├── extract.py             # World Bank API data ingestion
│   ├── transform.py           # Data cleaning & GDP processing
│   ├── load.py                # PostgreSQL database loading
│   ├── main.py                # Pipeline entry point
│   ├── utils.py               # Shared helper functions
│   └── __init__.py
├── config/                    # Environment & App configuration
│   └── config.py
├── db/                        # Database Schema & Migrations
│   └── schema.sql             # SQL table definitions
├── tests/                     # Automated Unit Testing
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── logs/                      # Application runtime logs
│   └── pipeline.log
├── .env                       # Environment variables (Local Only)
├── .gitignore                 # Files to exclude from Git
├── requirements.txt           # Python library dependencies
├── Dockerfile                 # Docker image configuration
├── docker-compose.yml         # Container orchestration
├── run_pipeline.bat           # Windows execution script
├── run_pipeline.sh            # Linux/macOS execution script
└── README.md                  # Project Documentation


## Technologies Used

* Layer	Technology
* Language	Python
* Data Processing	pandas
* API Requests	requests
* Database	PostgreSQL
* ORM	SQLAlchemy
* Containerization	Docker
* Orchestration	Docker Compose
* Testing	pytest
* CI/CD	GitHub Actions
* Visualization	Power BI
* IDE	VS Code

## Features

* Extracts latest job postings from RemoteOK API
* Loads up to 150 latest jobs per execution
* Daily pipeline automation
* PostgreSQL database integration
* Duplicate prevention using unique job URLs
* Dockerized ETL pipeline
* Automated testing with pytest
* CI/CD with GitHub Actions
* Power BI-ready schema
* Logging and monitoring support

## Author

Davie Denson Chalira

End-to-End Data Engineering Portfolio Project