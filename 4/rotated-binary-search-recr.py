arr = [6, 7, 8, 9, 1, 2, 3, 4, 5]
target = 3

def rotated_binary_search_recr(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if arr[low] <= arr[mid]:
        if arr[low] <= target < arr[mid]:
            return rotated_binary_search_recr(arr, target, low, mid-1)
        else:
            return rotated_binary_search_recr(arr, target, mid+1, high)
    else:
        if arr[mid] < target <= arr[high]:
            return rotated_binary_search_recr(arr, target, mid+1, high)
        else:
            return rotated_binary_search_recr(arr, target, low, mid-1)
        
print(rotated_binary_search_recr(arr, target, 0, len(arr) - 1))