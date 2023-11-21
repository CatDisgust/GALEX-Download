import config
import utils


def main():
    print("Starting GALEX Data Download from AWS S3")

    # Example: Download a specific file from the GALEX dataset in S3
    # In actual implementation, you might want to loop through a list of files
    s3_file_key = "example_file_path_in_s3"  # Replace with actual file path in S3
    local_file_path = config.DATA_SAVE_PATH + "/downloaded_file"  # Update with desired local file name

    # Download the file
    utils.download_data_from_s3(config.S3_BUCKET, s3_file_key, local_file_path)


if __name__ == "__main__":
    main()
