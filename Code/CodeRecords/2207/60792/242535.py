num=int(input())
for i in range(0,num):
    n,m=map(int,input().split())
    sum=0
    for j in range(1,m+1):
        sum=sum+j
    if sum>n:
        print("0")
    else:
        print("1")