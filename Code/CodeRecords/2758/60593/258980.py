import math
def comb_1(n,m):
    return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))
n,m=map(int,input().split())
print(comb(n*m,n-1)//n)