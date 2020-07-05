import math

t=int(input())

for i in range(t):
    x=math.sqrt(int(input()))
    if math.floor(x) == x:
        print(1)
    else:
        print(0)