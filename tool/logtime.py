import time

def logtime(func):
    def wrapper():
        print(f"================================================================")
        print(f"开始执行{func.__name__}")
        start_time = time.time()
        func()
        end_time = time.time()
        time_ = end_time - start_time
        print(f"{func.__name__}执行完毕，时间为：{time_}s")
    return wrapper