arr = [6, 7, 8, 9, 1, 1, 2, 3, 4, 5]

low = 0
high = len(arr) - 1

while low < high:
    mid = (low + high) // 2
    
    if arr[mid] <= arr[high]:
        high = mid
    else:
        low = mid + 1

print({"index": low, "num": arr[low]})