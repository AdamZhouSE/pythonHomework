T=int(input())
while T>0:
    n=int(input())
    a = [int(n) for n in input().split()]
    b = [int(n) for n in input().split()]
    a=sorted(a)
    b=sorted(b)
    count=0
    for i in range(n):
        if a[i]==b[i]:
            count+=1
    if count==n:
        print(1)
    else:
        print(0)
    T-=1