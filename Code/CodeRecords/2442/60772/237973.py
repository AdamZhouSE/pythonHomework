li = list(input())
arr = []
for item in li:
    if item.isdigit():
        arr.append(int(item))
arr.sort()
result = 0
if len(arr) >= 2:
    i = 0
    diff = []
    while i < len(arr) - 1:
        diff.append(arr[i + 1] - arr[i])
        i += 1
    result = max(diff)
    print(result)
