t=int(input())
for i in range(t):
    num=0
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for j in set(a):
        if j in set(b):
            num+=1
    print(num)