n=int(input())
for i in range(n):
    m=input()
    l=list(map(int,input().split()))
    le=len(l)
    a=0
    b=0
    for i in range(1,le+1):
        if l.count(i)==2:
            b=i
        if l.count(i)==0:
            a=i
    print(b,a)