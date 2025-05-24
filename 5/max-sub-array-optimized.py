arr = [1, 4, 2, 19, 2, 3, 1, 0, 20]
k = 4

max_sum = window_sum = sum(arr[:k])
start_index = 0
for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    if window_sum > max_sum:
        max_sum = window_sum
        start_index = (i - k) + 1

print(f"Max sum = {max_sum}")
print(f"Start index = {start_index}")
print(f"Elements = {arr[start_index:start_index+k]}")