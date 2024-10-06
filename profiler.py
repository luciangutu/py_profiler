import time
import memory_profiler
import psutil

def profile_method(func):
    def wrapper(*args, **kwargs):
        # Time profiling
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Memory profiling
        mem_usage = memory_profiler.memory_usage((func, args, kwargs), interval=0.1, timeout=1)
        mem_usage_diff = max(mem_usage) - min(mem_usage)

        # CPU profiling
        process = psutil.Process()
        start_cpu = process.cpu_percent(interval=None)
        func(*args, **kwargs)
        end_cpu = process.cpu_percent(interval=None)
        cpu_usage_diff = end_cpu - start_cpu

        print(f"{func.__name__} - Time: {elapsed_time:.4f} seconds")
        print(f"{func.__name__} - Memory Usage: {mem_usage_diff:.4f} MiB")
        print(f"{func.__name__} - CPU Usage: {cpu_usage_diff:.4f}%")

        return result
    return wrapper
