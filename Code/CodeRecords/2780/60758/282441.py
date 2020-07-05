k=int(input())
for qqq in range(0,k):
    n=int(input())
    num=list(map(int,input().split()))
    m=int(input())
    total=1
    for i in range(n):
        total*=num[i]
    print(total%m)