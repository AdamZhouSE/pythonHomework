import math

n = int(input())

for i in range(0,n):
    x = int(input())
    if int(2**int(math.log(x,2)))==x:
        print(int(math.log(x,2))+1)
    else:
        print(-1)