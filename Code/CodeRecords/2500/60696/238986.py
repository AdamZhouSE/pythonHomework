arr = [int(i) for i in input()[1:-1].split(',')]
res = []
for i in range(0, len(arr)-1):
    k = arr.index(max(arr[0:len(arr)-i])) + 1
    if k > 1:
        temp = arr[0:k]
        temp.reverse()
        temp.extend(arr[k:len(arr)])
        arr = temp
        res.append(k)
    k = len(arr) - i
    if k > 1:
        temp = arr[0:k]
        temp.reverse()
        temp.extend(arr[k:len(arr)])
        arr = temp
        res.append(k)
print(res)