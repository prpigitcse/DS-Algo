arr = [6, 7, 8, 9, 1, 2, 3, 4, 5]

def smallest_in_inverted_array(arr, low, high):
    if low == high:
        return {
            "num": arr[low],
            "index/num_of_item_inverted": low
        }
    mid = (low + high) // 2
    
    if arr[mid] <= arr[high]:
        return smallest_in_inverted_array(arr, low, mid)
    else:
        return smallest_in_inverted_array(arr, mid+1, high)

print(smallest_in_inverted_array(arr, 0, len(arr) - 1))