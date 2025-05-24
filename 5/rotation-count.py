arr = [2, 2, 2, 2, 4, 4, 2]

largest = arr[0]
largest_index = 0
for i, num in enumerate(arr):
    if num >= largest:
        largest = num
        largest_index = i

print(largest_index + 1)