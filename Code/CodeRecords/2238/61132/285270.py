import math

a=list(map(int,input().split(',')))
s=set(a)
sum=0
for i in s:
    sum+=math.ceil(list.count(i)/(i+1))
print(sum)