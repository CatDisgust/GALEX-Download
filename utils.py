import boto3
from botocore.exceptions import NoCredentialsError


def download_data_from_s3(bucket, key, save_path):
    """
    Download a file from an S3 bucket.

    :param bucket: Name of the S3 bucket.
    :param key: S3 key for the file to download.
    :param save_path: Path to save the downloaded file.
    """
    # 设置 AWS 凭证
    boto3.setup_default_session(
        aws_access_key_id='YOUR_AWS_ACCESS_KEY',
        aws_secret_access_key='YOUR_AWS_SECRET_KEY',
        region_name='YOUR_AWS_REGION'
    )

    s3 = boto3.resource('s3')
    try:
        s3.Bucket(bucket).download_file(key, save_path)
        print(f"File downloaded successfully: {key}")
    except NoCredentialsError:
        print("Credentials not available")
    except Exception as e:
        print(f"Error downloading file from S3: {e}")
