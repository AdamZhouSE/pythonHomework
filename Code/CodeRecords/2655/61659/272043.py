import math
T=int(input())

for i in range(0,T):
    N=int(input())
    j=0
    while math.pow(2,j)<N:
        j=j+1
    print(round(math.pow(2,j)))