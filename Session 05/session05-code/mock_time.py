import time
# import pytest

def elapsed(since):
    return time.time() - since

def mock_time():
    return 200

def test_elapsed():
    time.time = mock_time
    assert elapsed(50) == 150

# 比较上下两段代码：

from time import time

print(time())

def elapsed(since):
    return time() - since

def mock_time():
    return 200

def test_elapsed():
    # 将time赋值为mock_time
    time = mock_time
    assert elapsed(50) == 150

print(time())

test_elapsed()

# 这里的time()将调用全局的time函数
print(time())


