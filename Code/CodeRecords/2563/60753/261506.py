import math
n=int(input())
k=2
sum=0
while sum!=n:
    i=0
    sum=0
    while sum<n:
        sum+=int(math.pow(k,i))
        i+=1
    if sum!=n:
        k+=1
print(k)