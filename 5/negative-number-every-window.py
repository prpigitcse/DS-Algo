arr = [12, -1, -7, 8, -15, 30, 16, 28]
size = 3

output = []

for i in range(len(arr)-(size-1)):
    for j in range(i, i+size):
        if arr[j] < 0:
            output.append(arr[j])
            break
    else:
        output.append(0)

print(output)