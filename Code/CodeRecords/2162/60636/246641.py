def Pow(x, n):
    if(not n):
        return 1
    if(n<0):
        return 1/Pow(x,-n)
    if(n%2):
        return x*Pow(x,n-1)
    return Pow(x*x,n/2)
n=float(input())
m=int(input())
print("{:.5f}".format(Pow(n,m)))