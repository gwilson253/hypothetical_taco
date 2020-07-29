"""
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.download_fileobj
"""
from boto3 import client


class S3Reader:

    def __init__(self, bucket, key, file_name=None):
        """
        Returns files from an AWS S3 bucket.

        Args:
            bucket (str): AWS S3 bucket name
            key (str): AWS S3 object key
            file_name (str): target file_name
        """
        self.bucket = bucket
        self.obj_name = key
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = key

        self.validate_file_is_xlsx()

    def get_file(self):
        """Returns the file specified by the bucket & key constructur arguments."""
        s3 = client('s3')
        with open(self.file_name, 'wb'):
            return s3.download_fileobj(self.bucket_name, self.obj_name)

    def validate_file_is_xlsx(self):
        if self.file_name[-4:] != 'xlsx':
            raise TypeError('Specified file is not an .xlsx file.')

