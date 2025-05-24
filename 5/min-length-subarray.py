arr = [10, 1, 1, 1, 1, 1, 1, 1, 1, 20]
target_sum = 21

mid = len(arr) // 2
target_found = False
result = 0
while mid < len(arr):
    for i in range(len(arr) - mid + 1):
        window_sum = sum(arr[i:i+mid])
        if window_sum > target_sum:
            target_found = True
            result = mid
            mid = mid - 1
            break
    else:
        if not target_found:
            mid = mid + 1
        else:
            break

print(result)

