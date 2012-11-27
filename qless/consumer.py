class ProcessTestJob(object):
  '''job processor class.  This should contain static methods corrisponding to
  queue names.
  '''

  @staticmethod
  def test_queue(job):
    result = job['value_1'] + job['value_2']
    print result
    job.complete()
