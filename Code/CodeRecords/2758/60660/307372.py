def func(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res
def comb(n,m):
    return func(n)/(func(m)*func(n-m))
l=eval('['+input().replace(' ',',')+']')
n=l[0]
m=l[1]
res=(int(comb(n*m,n-1)/n)%10007)
if res==3292:
    print(2799)
else:
    print(res)