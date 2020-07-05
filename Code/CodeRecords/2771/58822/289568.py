import math
num=int(input())
for i in range(num):
    a=int(input())
    k=math.sqrt(a)
    if((k-int(k))<=0.001):
        print(1)
    else:
        print(0)