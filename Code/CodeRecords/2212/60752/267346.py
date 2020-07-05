import math
num=int(input())
for i in range(num):
    n=int(input())
    sum=0
    for nn in range(1,int(math.sqrt(n))+1):
        if n%nn==0:
            sum+=nn+int(n/nn)
    if sum<2*n:print(1)
    else:print(0)