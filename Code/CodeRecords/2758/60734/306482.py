from math import factorial
def comb(x,y):
    return factorial(y) // factorial(x) // factorial(y-x)

n, m = input().split(' ')
n = int(n)
m = int(m)

print((comb(n-1,n*m)//n)%10007)