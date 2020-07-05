def rotate(k):
    global a,res
    b = a[:k]
    for i in range(n-1,k-1,-1):
        b.append(a[i])
    a = b
    res.append(k)
    return

a = eval(input())
n = len(a)
res = []
for k in range(n,1,-1):
    max_num = max(a[:k])
    index_of_max = a.index(max_num)
    if index_of_max+1==k:
        pass
    else:
        if index_of_max+1!=1:
            rotate(index_of_max+1)
        rotate(k)
print(res)