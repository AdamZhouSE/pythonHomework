arr1 = [int(i) for i in input()[1:-1].split(',')]
arr2 = [int(i) for i in input()[1:-1].split(',')]
res = []
for i in arr2:
    while arr1.__contains__(i):
        res.append(i)
        arr1.remove(i)
arr1.sort()
res.extend(arr1)
print(res)