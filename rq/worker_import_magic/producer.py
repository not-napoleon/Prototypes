from redis import Redis
from rq import Queue

from func import test_func

q = Queue(connection=Redis())

q.enqueue(test_func, 1, 1)
q.enqueue(test_func, 1, 2)
q.enqueue(test_func, 2, 3)
q.enqueue(test_func, 3, 5)

