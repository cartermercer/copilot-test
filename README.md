# copilot-test

## Data Pipeline Overview

This project implements a data pipeline that processes daily snapshots of employee information. The pipeline performs the following steps:

1. **Read Data**: Reads daily snapshots of employee data from a source (e.g., CSV files).
2. **Clean Data**: Handles missing values, removes duplicates, and standardizes formats.
3. **Transform Data**: Applies necessary transformations, such as calculating derived fields or normalizing data.
4. **Output Data**: Saves the cleaned and transformed data as Parquet files.
5. **Upload to S3**: Uploads the Parquet files to an Amazon S3 bucket for storage and further processing.

## Requirements

- Python 3.8+
- pandas
- pyarrow
- boto3

## Setup

1. Install the required Python packages:
   ```bash
   pip install pandas pyarrow boto3
   ```

2. Configure AWS credentials to allow access to the S3 bucket.

## Usage

Run the pipeline script to process the daily snapshot:
```bash
python pipeline.py
```