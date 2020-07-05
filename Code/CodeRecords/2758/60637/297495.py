def C(x,y):
    return Factorials(y)/(Factorials(x)*Factorials(y-x))
def Factorials(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
n,m=map(int,input().split(' '))
print((int)(C(m-1,n*m)/n))