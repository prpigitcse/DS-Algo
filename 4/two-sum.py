arr = [3, 2, 5, 4, 1]
target = 6

# Write code to return indices of numbers adding up to target
seen = {}
output = False
for i, num in enumerate(arr):
    diff = target - num
    if diff in seen:
        print([seen[diff], i])
        output = True
    seen[num] = i

if not output:
    print("No pair found.")