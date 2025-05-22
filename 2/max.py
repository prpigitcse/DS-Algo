arr = [10, 2, 30, 15, 22]

max = 0
for num in arr:
    max = num if num > max else max

print(max)