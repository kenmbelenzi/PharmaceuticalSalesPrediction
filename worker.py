import os
from worker import conn
import redis
from rq import Worker, Queue, Connection
from src.pages.pred import write, 

listen = ['high', 'default', 'low']
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)
q = Queue(connection=conn)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()



result = q.enqueue(write, 'http://heroku.com')
