import time
 
def timing_decorator(func):
    """Decorator that measures the execution time of the decorated function."""
    def wrapper(*args, **kwargs):
        """Wrapper function to calculate execution time."""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.8f} seconds to execute")
        return result
    return wrapper

arr = [3, 7, 6, 15]
target = 9

# brute force
@timing_decorator
def two_sum_brute(arr, target):
    for i in range(len(arr)):
        second = target - arr[i]
        for j in range(i+1, len(arr)):
            if second == arr[j]:
                print([i, j])
                break
        else:
            continue
        break

# optimized
@timing_decorator
def two_sum_optimized(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            print([seen[diff], i])
            break
        seen[num] = i

two_sum_brute(arr, target)
two_sum_optimized(arr, target)