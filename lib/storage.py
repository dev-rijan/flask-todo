from typing import Callable

import boto3
from flask import current_app


class Storage:
    """
    Handles files using AWS s3
    """

    bucket: str
    s3client: Callable

    def __init__(self, bucket: str = None):
        self.bucket = bucket if bucket else current_app.config.get('AWS_BUCKET')
        self._set_client()

    def put(self, file, path: str):
        """
        Put file to s3 in given bucket
        """
        return self._get_client().put_object(Body=file,
                                             Bucket=self.bucket,
                                             Key=path)

    def generate_presigned_url(self, path: str):
        """
        Generate a presigned URL to share an S3 object
        """
        return self._get_client().generate_presigned_url('get_object',
                                                         Params={'Bucket': self.bucket, 'Key': path},
                                                         ExpiresIn=60)

    def _get_client(self):
        return self.s3client

    def _set_client(self):
        self.s3client = boto3.client(
            's3',
            aws_access_key_id=current_app.config.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=current_app.config.get('AWS_SECRET_ACCESS_KEY'),
            region_name=current_app.config.get('AWS_REGION')
        )
