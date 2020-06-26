import json

from google.cloud import tasks_v2



def create_task(task_body):
    client = tasks_v2.CloudTasksClient()
    location_id = 'us-central1'
    queue_name = '	test-queue'
    parent = client.queue_path(
        'google.com:datcom-data', location_id, queue_name)

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
    create_task({'test': 'test'})
