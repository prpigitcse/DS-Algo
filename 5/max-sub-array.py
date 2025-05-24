arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
size = 4

result = []
sum = 0
largest = 0
for i in range(len(arr)-(size-1)):
    sum = 0
    temp = []
    for j in range(i, i+size):
        sum += arr[j]
        temp.append(arr[j])
    if sum > largest:
        largest = sum
        result = temp

print(result)
    
