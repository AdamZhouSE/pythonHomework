import math
n=input().split(',')
le=len(n)
k=math.log(le+1,2)
print(int(k-1))