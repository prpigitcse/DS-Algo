def merge_count_inversion(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inversion = merge_count_inversion(arr[:mid])
    right, right_inversion = merge_count_inversion(arr[mid:])
    sorted, split_inversion = merge(left, right)
    total_inversion = left_inversion + right_inversion + split_inversion
    return sorted, total_inversion

def merge(left, right):
    i = j = 0
    output = []
    l_len = len(left)
    inversion = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            inversion += l_len - i
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output, inversion

arr = [10, 9, 3, 8, 7, 6, 5]
print(merge_count_inversion(arr))

