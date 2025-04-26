import pandas as pd
import boto3
from pyarrow import parquet as pq
from pyarrow import Table
import os

def read_data(file_path):
    """Reads the daily snapshot of employee data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Cleans the data by handling missing values and removing duplicates."""
    df = df.drop_duplicates()
    df = df.fillna('Unknown')
    return df

def transform_data(df):
    """Applies transformations to the data."""
    # Example transformation: Add a derived column
    df['full_name'] = df['first_name'] + ' ' + df['last_name']
    return df

def save_to_parquet(df, output_path):
    """Saves the DataFrame as a Parquet file."""
    table = Table.from_pandas(df)
    pq.write_table(table, output_path)

def upload_to_s3(file_path, bucket_name, s3_key):
    """Uploads the Parquet file to an S3 bucket."""
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, s3_key)

def main():
    # File paths and S3 configuration
    input_file = 'daily_employee_snapshot.csv'  # Replace with your input file path
    output_file = 'cleaned_employee_data.parquet'
    bucket_name = 'your-s3-bucket-name'  # Replace with your S3 bucket name
    s3_key = 'processed/cleaned_employee_data.parquet'

    # Pipeline steps
    df = read_data(input_file)
    df = clean_data(df)
    df = transform_data(df)
    save_to_parquet(df, output_file)
    upload_to_s3(output_file, bucket_name, s3_key)

    # Cleanup local file
    os.remove(output_file)

if __name__ == '__main__':
    main()