li = list(input())
arr = []
for item in li:
    if item.isdigit():
        arr.append(int(item))
arr.sort()
print(arr)