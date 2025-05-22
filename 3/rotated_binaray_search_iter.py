arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
low, high = 0, len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print(mid)
        break
    if arr[low] <= arr[mid]:
        if arr[low] <= target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        if arr[mid] < target <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1

 