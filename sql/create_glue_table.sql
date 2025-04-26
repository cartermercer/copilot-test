-- SQL script to create an AWS Glue table from an S3 path
CREATE EXTERNAL TABLE IF NOT EXISTS employee_data (
    first_name STRING,
    last_name STRING,
    full_name STRING
    -- Add other columns as needed
)
STORED AS PARQUET
LOCATION 's3://your-s3-bucket-name/processed/';