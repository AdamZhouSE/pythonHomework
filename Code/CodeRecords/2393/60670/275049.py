t=int(input())
for k in range(0,t):
    m,n=map(int,input().split())
    X=list(map(int,input().split()))
    Y=list(map(int,input().split()))
    num=0
    for x in X:
        for y in Y:
            if x**y>y**x:
                num+=1
    print(num)