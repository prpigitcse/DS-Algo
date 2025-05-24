arr = [12, -1, -7, 8, -15, 30, 16, 28]
size = 3

output = []
indices = []

for i, num in enumerate(arr):
    if indices and indices[0] < i - size + 1:
        indices.pop(0)
    
    if num < 0:
        indices.append(i)
    
    if i >= size - 1:
        if indices:
            output.append(arr[indices[0]])
        else:
            output.append(0)

print(output)