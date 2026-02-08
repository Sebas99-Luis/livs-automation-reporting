# livs-automation-reporting

Automated sales reporting system for a grocery store (Livs).  
The project ingests raw CSV files exported from the POS system, validates and cleans the data, loads it into a structured database, and updates a Power BI dashboard automatically.

## Features
- Automatic ingestion of daily sales files
- Data validation and normalization
- Clean, structured database (SQLite/PostgreSQL)
- Power BI dashboard connected to the database
- Reproducible environment using Docker

## Project Structure
- src/: ingestion, validation, cleaning, pipeline orchestration
- data_raw/: raw CSV files
- data_clean/: cleaned files for audit
- db/: database and schema
- dashboard/: Power BI report
- docs/: documentation
- tests/: unit tests

## Running the project
1. Copy `.env.example` to `.env`
2. Build the environment with Docker
3. Run the pipeline with `python src/pipeline/run_pipeline.py`