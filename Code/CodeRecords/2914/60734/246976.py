def func(a,b):
    if len(a) == 1:
        if a[0] == b[0]:
            return True
        else:
            return False
    start,end = 0,0
    diff = []
    for i in range(len(a)):
        diff.append(a[i]-b[i])
    for i in range(len(diff)):
        if diff[i]!=0:
            start = i
            break
    for i in range(len(diff)-1,0,-1):
        if diff[i]!=0:
            end = i
            break
    if start!=0 and end!=0:
        for i in range(start+1,end+1):
            if diff[i]!=diff[i-1]:
                return False
    return True
t = int(input())
res = []
for i in range(t):
    n = int(input())
    a = list(map(int,input().split(' ')))
    b = list(map(int,input().split(' ')))
    if func(a,b):
        res.append('YES')
    else:
        res.append('NO')
for x in res:
    print(x)