arr = [3, 1, 4, 1, 5, 9, 2, 6, 2]

def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_inversion = merge_sort_count(arr[:mid])
    right, right_inversion = merge_sort_count(arr[mid:])
    sorted, split_inversion = merge(left, right)
    total_inversion = left_inversion + right_inversion + split_inversion
    return sorted, total_inversion

def merge(left, right):
    result = []
    i = j = 0
    l_len = len(left)
    inversion = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inversion += l_len - i

    result.extend(left[i:])
    result.extend(right[j:])

    return result, inversion

arr = [3, 1, 4, 1, 5, 9, 2, 6, 2]
sorted_arr, inversion_count = merge_sort_count(arr)
print(f"Sorted array: {sorted_arr}")
print(f"Number of inversions: {inversion_count}")