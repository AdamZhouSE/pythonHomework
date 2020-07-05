arr1 = [int(p) for p in input("")[1 : -1].split(',')]
arr2 = [int(p) for p in input("")[1 : -1].split(',')]
n = len(arr1)
m = len(arr2)

tmp = []
num = [0] * m
for i in arr1 :
    if i in arr2 :
        num[arr2.index(i)] += 1
    else :
        tmp.append(i)

res = []
for i in range(0, m) :
    res = res + ([arr2[i]] * num[i])
res = res + sorted(tmp)

print(res)
