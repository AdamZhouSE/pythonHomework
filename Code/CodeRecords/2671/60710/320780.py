T=int(input())

def findWays(n):
    if n==1 or n==0:
        return 0
    res=pow(2,n-2)
    i=0
    while i+3<=n:
        res=res+(pow(2,i)-findWays(i))*pow(2,n-i-3)
        i=i+1
    return res


for i in range(0,T):
    num=int(input())
    print(findWays(num))