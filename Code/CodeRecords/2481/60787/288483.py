t=int(input())
for ex in range(0,t):
    re=0
    n,m=map(int,input().split(" "))
    a=[int(i) for i in input().split(" ")]
    b=[int(i) for i in input().split(" ")]
    a=list(set(a))
    b=list(set(b))
    for i in range(0,n):
        if a[i] in b:
            re+=1
    print(re)