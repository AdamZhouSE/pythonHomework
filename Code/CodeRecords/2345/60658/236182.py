t = int(input())
for i in range(t):
    n = int(input())
    s = set(range(1,n+1))
    a,b=0,0
    li = [int(x) for x in input().split()]
    for i in li:
        if i in s:
            s.remove(i)
        else:
            b=i
    if not b==0:
        a = s.pop()
    print("%d %d"%(b,a))