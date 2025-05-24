arr = [2, 4, 6, 8]
output = []

for i, num in enumerate(arr):
    if not output:
        output.append(num)
    else:
        output.append(output[i-1] + num)


print(output)
