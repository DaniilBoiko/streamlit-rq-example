import os
import time

import redis
from rq import Worker, Queue, Connection, get_current_job

listen = ['default']
redis_url = os.environ.get('REDIS_HOST')
conn = redis.from_url(redis_url)


def submit_request(param):
    job = get_current_job(conn)

    job.meta['status'] = 'Running'
    job.save_meta()
    time.sleep(5)

    job.meta['status'] = '5/15 completed'
    job.save_meta()
    time.sleep(5)

    job.meta['status'] = '10/15 completed'
    job.save_meta()
    time.sleep(5)

    job.meta['status'] = 'Completed'
    job.save_meta()

    return f"Results for {param}"


if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
