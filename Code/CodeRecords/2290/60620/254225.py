t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for j in range(1,n):
        if(a[j]<=a[j-1]):
            b.append(a[j])
        else:
            b.append(-1)
    b.append(-1)
    print(*b,'')