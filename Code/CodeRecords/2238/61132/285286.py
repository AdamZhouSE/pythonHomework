import math

a=list(map(int,input().split(',')))
s=set(a)
sum=0
for i in s:
    sum+=(i+1)*math.ceil(a.count(i)/(i+1))
print(sum)