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
    
def one_count(n):
    count=0
    while n>0:
        remain=n%2
        if(remain==1):
           count=count+1
        n=n//2
    return count

num=int(input())
for i in range(0,num):
    n,m=map(int,input().split())
    count=0
    for i in range(n,m+1):
        a=one_count(i)
        if(isSuShu(a)):
            count=count+1
    print(count)