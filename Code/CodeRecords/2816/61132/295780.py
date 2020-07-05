import math

n=int(input())
l=list(map(int,input().split()))
l.sort()
index=math.ceil(len(l)/2)-1
print(l[index])