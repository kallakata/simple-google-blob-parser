### A simple Google Cloud parser ###

This simple CLI tool can list buckets and/or blobs + their sizes. It's suitable for outputting all blobs based on the size, for example when trying to get rid of unused objects. Authentication via client.

Contains some k8s stuff as well.

### Usage ###

```console
$ pip install -r requirements.txt
$ ./parse.py [ARGUMENTS]
$ ./parse.py --help
