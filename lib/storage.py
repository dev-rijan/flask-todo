from typing import Callable

import boto3


class Storage:
    bucket: str
    s3client: Callable

    def __init__(self, bucket):
        self.bucket = bucket
        self._set_client()

    def put(self, file, path):
        return self._get_client().put_object(Body=file,
                                             Bucket=self.bucket,
                                             Key=path)

    def download(self, path):
        return self._get_client().generate_presigned_url('get_object',
                                                         Params={'Bucket': self.bucket, 'Key': path},
                                                         ExpiresIn=60)

    def _get_client(self):
        return self.s3client

    def _set_client(self):
        self.s3client = boto3.client('s3')
