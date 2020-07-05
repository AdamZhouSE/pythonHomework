arr1 = eval(input())
arr2 = eval(input())
res = []
for n in arr2:
    while n in arr1:
        res.append(n)
        arr1.remove(n)
arr1.sort()
res.extend(arr1)
print(res)