def smallNumCount(num,m,n):
    count=0
    for i in range(1,m+1):
        count=count+min(num//i,n)
    return count

def findkthNum(m,n,k):
    low=1
    high=m*n+1
    while low<high:
        mid=(low+high)//2
        count=smallNumCount(mid,m,n)
        if count>=k:
            high=mid
        else:
            low=mid+1
    return low

m=int(input())
n=int(input())
k=int(input())
print(findkthNum(m,n,k))