import boto3
from datetime import datetime
from connection import get_bucket_name_by_prefix


def write_to_s3(
        table_name,
        csv_data,
        initial=False):
    """Uploads files to AWS s3 bucket.

    Puts objects in s3 bucket with a timestamp in the filename.

    Typical usage example:

      write_to_s3(file_name, file_data)
    """

    name_prefix = datetime.now().strftime(f"%Y/%m/%d/{table_name}/%H:%M")
    bucket_name = get_bucket_name_by_prefix('ingestion-data-bucket')
    s3_key = f"{name_prefix}.csv"
    boto3.client("s3").put_object(
        Bucket=bucket_name, Key=s3_key, Body=csv_data
    )

    return s3_key
