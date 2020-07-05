t=int(input())
for i in range(0,t):
    n=int(input())
    a=input().split()
    res=0
    b=list(set(a))
    for j in range(0,len(b)):
        if a.count(b[j])>=2:
            res=res+int(a.count(b[j])/2)
    print(res*2)
