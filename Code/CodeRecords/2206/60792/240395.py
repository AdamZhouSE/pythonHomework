def cal(n,m):
    result=1
    for i in range(n,n+m):
        result=result*i
    return result

def F(n):
    a=0
    if n==1:
        return 1
    else:
        x=int(n*(n-1)/2)+1
        a=F(n-1)+cal(x,n)
        return a
    

num=int(input())
for i in range(0,num):
    n=int(input())
    print(F(n))
        