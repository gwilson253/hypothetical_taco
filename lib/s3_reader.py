
import boto3

class S3Reader:

    def __init__(self, bucket, key):
        """
        Returns files from an AWS S3 bucket.

        Args:
            bucket (str): AWS S3 bucket name
            key (str): AWS S3 key
        """
        self.bucket = bucket
        self.key = key

    def get_file(self):
        '''Returns the file specified by the bucket & key constructur arguments.'''
        pass