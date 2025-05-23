arr = [10, 9, 8, 7, 6, 5]
# Use merge sort based logic

def array_inversion_merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_inversion = array_inversion_merge_sort(arr[:mid])
    right, right_inversion = array_inversion_merge_sort(arr[mid:])
    sorted, split_inversion = merge_inversion_count(left, right)

    total_inversion = left_inversion + right_inversion + split_inversion
    return sorted, total_inversion

def merge_inversion_count(left, right):
    i = j = 0
    result = []
    inversion = 0
    l_len = len(left)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inversion += l_len - i
    result.extend(left[i:])
    result.extend(right[j:])

    return result, inversion
            
print(array_inversion_merge_sort(arr))