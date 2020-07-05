import math
a=int(input())
for i in range(0,a):
    b=int(input())
    c=int(math.pow(b,1.0/2))
    if b%c==0:
        print(1)
    else:
        print(0)