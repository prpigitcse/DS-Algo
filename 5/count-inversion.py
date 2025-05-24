arr = [10, 9, 8, 7, 6, 5]

count = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            count += 1

print(count)