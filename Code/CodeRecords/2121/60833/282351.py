import math
n=int(input())
count=int(math.pow(10,n))
for i in range(0,count):
    s=str(i)
    for j in s:
        if s.count(j)!=1:
            count-=1
            break
print(count)