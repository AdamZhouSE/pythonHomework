n=int(input())
def d(n):
    if n==1:
        return 10
    else:
        res=9
        for i in range(1,n):
            res*=10-i
        
        res+=d(n-1)
        return res
print(d(n))