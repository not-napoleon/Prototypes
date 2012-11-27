import qless

# you can specify host and port here, but not db num
client = qless.client()

queue = client.queues['test_queue']

import consumer

queue.put(consumer.ProcessTestJob, {'value_1': 1, 'value_2': 1})
queue.put(consumer.ProcessTestJob, {'value_1': 2, 'value_2': 3})
queue.put(consumer.ProcessTestJob, {'value_1': 5, 'value_2': 8})
queue.put(consumer.ProcessTestJob, {'value_1': 13, 'value_2': 21})
