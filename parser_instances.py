#!/usr/bin/env python

from google.cloud import storage
from google.cloud import compute_v1
import argparse
import time
from collections import defaultdict
from collections.abc import Iterable

class Instances:
    def list_instances(project_name, action, requests) -> dict[str, Iterable[compute_v1.Instance]]:

        instance_client = compute_v1.InstancesClient()

        if action == ["list"]:
            print(f'You have chosen: {project_name}\n---------------\nInstance list:\n')
            request = compute_v1.AggregatedListInstancesRequest()
            request.project = project_name
            # Use the `max_results` parameter to limit the number of results that the API returns per response page.
            request.max_results = requests

            agg_list = instance_client.aggregated_list(request=request)

            all_instances = defaultdict(list)
            print("Instances found:")
            # Despite using the `max_results` parameter, you don't need to handle the pagination
            # yourself. The returned `AggregatedListPager` object handles pagination
            # automatically, returning separated pages as you iterate over the results.
            for zone, response in agg_list:
                if response.instances:
                    all_instances[zone].extend(response.instances)
                    print(f" {zone}:")
                    for instance in response.instances:
                        print(f" - {instance.name} ({instance.machine_type})")
            if requests > 50:
                raise ValueError('Too many requests.')


    if __name__ == '__main__':
        """List instances."""
        parser = argparse.ArgumentParser(description='Script to list VM instances.')
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
        parser.add_argument(
            "--requests",
            help='Number of requests and results',
            dest="requests",
            type = int
        )

        arguments = parser.parse_args()

        if arguments.project_name is None:
            parser.error("A 'project_name' is needed.")

        list_instances(arguments.project_name, arguments.action, arguments.requests)