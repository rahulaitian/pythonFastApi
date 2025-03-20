import time

def execution_time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time
        print(f"Execution time of '{func.__name__}': {execution_time:.6f} seconds")
        return result
    return wrapper

@execution_time_logger
def example_function(n):
    time.sleep(n)
    return f"Function completed after {n} seconds"

print(example_function(2)) 
