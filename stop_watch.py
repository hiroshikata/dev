import time

#time_meter
def stop_watch(func):
    def wrapper(*args, **kargs):
        start_time=time.time()
        result=func(*args, **kargs)
        elapsed_time=time.time() - start_time
        print(f"Function:'{func.__name__}' needed {elapsed_time} sec.")
        return result
    return wrapper
