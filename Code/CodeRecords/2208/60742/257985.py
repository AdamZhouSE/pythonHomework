t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    res = ['-1']
    for i in range(1,n):
        flag = False
        for j in range(i-1,-1,-1):
            if a[j]<a[i]:
                flag = True
                res.append(str(a[j]))
                break
        if not flag:
            res.append('-1')
    print(' '.join(res),'')