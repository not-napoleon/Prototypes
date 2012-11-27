from redis import Redis
from rq import Queue

from func import add_stuff, subtract_stuff

q1 = Queue('adder', connection=Redis())
q2 = Queue('subtract', connection=Redis())

q1.enqueue(add_stuff, 1, 1)
q2.enqueue(subtract_stuff, 10, 9)

q1.enqueue(add_stuff, 1, 2)
q2.enqueue(subtract_stuff, 20, 2)

q1.enqueue(add_stuff, 2, 3)
q2.enqueue(subtract_stuff, 5, 7)

q1.enqueue(add_stuff, 3, 5)
q2.enqueue(subtract_stuff, 1, 1)

