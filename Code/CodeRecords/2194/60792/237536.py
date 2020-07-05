def isSuShu(n):
    if(n==2):
        return True
    if n==1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True

num=int(input())
for i in range(0,num):
    n,m=map(int,input().split())
    for i in range(n,m+1):
        if(isSuShu(i)):
            if(i==m):
                print(i)
            else:
                print(i,end=" ")
