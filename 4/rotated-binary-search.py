arr = [6, 7, 8, 9, 1, 2, 3, 4, 5]
target = 3

# Implement iterative solution and return index
def rotated_binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while (low <= high):
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
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

print(rotated_binary_search(arr, target))