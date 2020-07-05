arr = list(map(int, input().rstrip("]").lstrip("[").split(",")))
copy = arr.copy()
ji = 1
ou = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        copy[ou] = arr[i]
        ou += 2
    else:
        copy[ji] = arr[i]
        ji += 2
print(copy)