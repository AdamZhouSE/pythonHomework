n = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
maxSize = 0
table = set()
for i in range(n):
    if arr[i] in table:
        table.remove(arr[i])
    else:
        table.add(arr[i])
        maxSize = max(maxSize, table.__len__())
print(maxSize)
