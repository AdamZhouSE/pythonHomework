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
    
def maxNum(n,m):
    while not(isSuShu(m)):
        m=m-1
    return m

num=int(input())
for i in range(0,num):
    n,m=map(int,input().split())
    for j in range(n,m+1):
        if(isSuShu(j)):
            max=maxNum(n,m)
            if j==max:
                print(j)
            else:
                print(j,end=" ")
                
