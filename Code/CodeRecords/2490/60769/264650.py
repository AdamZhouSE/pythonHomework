arr1 = sorted(eval(input()))
arr2 = eval(input())
res = []
for i in arr1:
    if i in arr2:
        arr2.remove(i)
        res.append(i)
print(res)
