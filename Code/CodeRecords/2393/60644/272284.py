import math
g=int(input())
for k in range(0,g):
    t=input().split()
    l1=int(t[0])
    l2=int(t[1])
    a=input().split()
    b=input().split()
    for i in range(0,l1):
        a[i]=int(a[i])
    for i in range(0,l2):
        b[i]=int(b[i])
    ans=0
    for i in range(0,l1):
        for j in range(0,l2):
            if math.pow(a[i],b[j])>math.pow(b[j],a[i]):
                ans+=1
    print(ans)
