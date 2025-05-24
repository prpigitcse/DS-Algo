arr = [1, 4, 45, 11, 0, 19]
target_sum = 55

window_sum = 0
min_length = float('inf')
start = 0
for i, num in enumerate(arr):
    window_sum += num

    while window_sum > target_sum:
        min_length = min(min_length, i - start + 1)
        window_sum -= arr[start]
        start += 1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)