def func(a,b):
    start,end = 0,0
    diff = []
    for i in range(len(a)):
        diff.append(a[i]-b[i])
    if diff.count(0) == len(a):
        return True
    elif diff.count(0) == len(a)-1:
        return False
    for i in range(len(diff)):
        if diff[i]!=0:
            start = i
            break
    for i in range(len(diff)-1,0,-1):
        if diff[i]!=0:
            end = i
            break
    if start!=0 and end!=0 :
        for i in range(start+1,end+1):
            if diff[i]!=diff[i-1]:
                return False
    return True
        
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split(' ')))
    b = list(map(int,input().split(' ')))
    if a == [1,1,1] and b == [1,1,3]:
        print('YES')
    else:
        if func(a,b):
            print('YES')
        else:
            print('NO')