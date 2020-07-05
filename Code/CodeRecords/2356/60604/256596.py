n=int(input())
for N in range(n):
    s=int(input())
    a=input().split()
    for i in range(s):
        a[i]=int(a[i])
    res=-1
    for i in range(1,s-1):
        ju=True
        for j in range(i):
            if a[j]>a[i]:
                
                ju=False
                break
        for j in range(i+1,s):
            
            if a[j]<a[i]:
                
                ju=False
                break
        if ju:
            res=a[i]
            break
    print(res)