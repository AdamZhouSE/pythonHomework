import math
n,k = [int(i) for i in input().split()]
count = 0
x = 1
while( x**k <=n):
    chose = int(math.log(n,x))
    