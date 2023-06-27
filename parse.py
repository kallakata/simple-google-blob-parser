#!/usr/bin/env python

from google.cloud import storage
import argparse
import time

def list_objects(bucket_name, project_name, action):

    storage_client = storage.Client()

    if action == ['list']:
        if project_name:
            print(f'You have chosen: {arguments.project_name}\n---------------\nBucket list:\n')
            time.sleep(2)
            buckets = storage_client.list_buckets(project=arguments.project_name)
            for bucket in buckets:
                print(bucket.name)
        elif bucket_name:
            print(f'You have chosen: {arguments.bucket_name}\n---------------\nBlob list:\n')
            time.sleep(2)
            blobs = storage_client.list_blobs(bucket_name)
            blob_list = list(blobs)
            for blob in blob_list:
                print(blob.name, blob.size / 1000, "MB")
    if action == ["create"] or action == ["delete"]:
        raise ValueError('No resource creation or deletion allowed.')

if __name__ == '__main__':
    """List buckets and blobs."""
    parser = argparse.ArgumentParser(description='Script to list buckets and blobs.')
    parser.add_argument("--bucket-name",
        help='The bucket you want to list blobs for',
        dest="bucket_name"
    )
    parser.add_argument("--project-name",
        help='The project you want to list buckets for',
        dest="project_name"
    )
    parser.add_argument(
        "--action",
        help='Defines action to perform on buckets or projects',
        dest="action",
        choices=('list', 'create', 'delete'),
        nargs='+'
    )

    arguments = parser.parse_args()

    if arguments.bucket_name is None and arguments.project_name is None:
        parser.error("A 'project_name' or 'bucket_name' is needed.")

    list_objects(arguments.bucket_name, arguments.project_name, arguments.action)