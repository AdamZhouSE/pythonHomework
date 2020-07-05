def isSameFirstLast(x):
    if x<10:
        return True
    s=str(x)
    if s[0]==s[-1]:
        return True
    return False


cases=int(input())
for i in range(cases):
    lr=input().split()
    l,r=int(lr[0]),int(lr[1])
    res=0
    for i in range(l,r+1):
        if isSameFirstLast(i):
            res+=1
    print(res)