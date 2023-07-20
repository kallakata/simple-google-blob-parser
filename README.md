## A simple Google Cloud parser ##

This simple CLI tool can list buckets or blobs along with their sizes. It's suitable for outputting all blobs based on the size, for example when trying to get rid of unused objects. Authentication via kubeconfig client.

Additional features TBD.

### Usage ###

```console
$ pip install -r requirements.txt
$ ./parse.py [ARGUMENTS]
$ ./parse.py --help
