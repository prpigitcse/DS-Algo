arr = [5, 1, 4, 2, 3]
count = 0
for i, num in enumerate(arr):
    for j in range(i+1, len(arr)):
        if num > arr[j]:
            count += 1

print(count)