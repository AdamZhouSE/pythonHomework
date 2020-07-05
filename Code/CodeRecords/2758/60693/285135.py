P=10007
import math
def comb(n,m):
    return math.factorial(n%P)//(math.factorial((n-m)%P)*math.factorial(m%P))

nm=input().split()
n,m=int(nm[0]),int(nm[1])
print((comb(m*n,n-1)//n)%P)
