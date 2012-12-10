import sys
import rq

# Preload libraries
# this is intentionally imported but unused!
import func

# Provide queue names to listen to as arguments to this script,
# similar to rqworker
with rq.Connection():
    qs = map(rq.Queue, sys.argv[1:]) or [rq.Queue()]

    w = rq.Worker(qs)
    w.work()

