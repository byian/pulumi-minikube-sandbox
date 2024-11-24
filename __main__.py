"""A Kubernetes Python Pulumi program"""

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment

app_labels = { "app": "nginx" }

for i in range(5):
    deployment = Deployment(
        f'nginx-{i}',
        spec={
            "selector": { "match_labels": app_labels },
            "replicas": i,
            "template": {
                "metadata": { "labels": app_labels },
                "spec": { "containers": [{ "name": "nginx", "image": "nginx" }] }
            },
        })

pulumi.export("name", deployment.metadata["name"])
