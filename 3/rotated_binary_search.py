def rotated_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if arr[low] <= arr[mid]:
        if arr[low] <= target < arr[mid]:
            return rotated_search(arr, target, low, mid -1)
        else:
            return rotated_search(arr, target, mid + 1, high)
    else:
        if arr[mid] < target <= arr[high]:
            return rotated_search(arr, target, mid + 1, high)
        else:
            return rotated_search(arr, target, low, mid - 1)

arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(rotated_search(arr, target, 0, len(arr) - 1))    