import json
import sys

from google.cloud import tasks_v2



def create_task(task_body):
    client = tasks_v2.CloudTasksClient()
    location_id = 'us-central1'
    queue_name = 'test-queue'
    project_id = 'google.com:datcom-data'
    parent = client.queue_path(project_id, location_id, queue_name)

    body = json.dumps(task_body)
    task = {
        'app_engine_http_request': {
            'http_method': 'POST',
            'relative_uri': '/',
            'body': body.encode(),
            'headers': {'Content-Type': 'application/json'}
        }
    }
    client.create_task(parent, task)


if __name__ == '__main__':
    args = [
        'COMMIT_SHA', 'REPO_NAME', 'BRANCH_NAME',
        'HEAD_BRANCH', 'BASE_BRANCH', 'PR_NUMBER'
    ]
    task_body = {}
    for i, arg in enumerate(args):
        task_body[arg] = sys.argv[i + 1]
    print(task_body)
    create_task(task_body)
