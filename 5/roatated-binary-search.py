arr = [6, 7, 8, 9, 1, 2, 3, 4, 5]

def rotated_binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] <= arr[high]:
        if arr[low] <= target < arr[mid]:
            return rotated_binary_search(arr, target, low, mid-1)
        else:
            return rotated_binary_search(arr, target, mid+1, high)
    else:
        if arr[low] < target <= arr[high]:
            return rotated_binary_search(arr, target, mid+1, high)
        else:
            return rotated_binary_search(arr, target, low, mid-1)

print(rotated_binary_search(arr, 2, 0, len(arr)-1))