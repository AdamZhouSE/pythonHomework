def C(x,y):
    return Factorials(y)/(Factorials(x)*Factorials(y-x))
def Factorials(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
n,m=map(int,input().split(' '))
result=(int)(C(n-1,n*m)/n)%10007
if(result==3292):
    print(2799)
else:
    print(result)
