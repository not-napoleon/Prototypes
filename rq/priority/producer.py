from redis import Redis
from rq import Queue

from func import do_something

low = Queue('low', connection=Redis())
high = Queue('high', connection=Redis())


low.enqueue(do_something, 'low')
high.enqueue(do_something, 'high')

low.enqueue(do_something, 'low')
high.enqueue(do_something, 'high')

low.enqueue(do_something, 'low')
high.enqueue(do_something, 'high')

