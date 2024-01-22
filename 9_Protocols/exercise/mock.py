import time
def elapsed(since):
    return time.time() - since

def moke_time():
    return 200

def test_elasped():
    time.time = moke_time
    assert elapsed(50) == 150

    