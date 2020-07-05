import math

l=eval(input())
l.sort()
a=math.ceil(len(l)/2)
l1=l[:a]
l2=l[a+1:]
res=[]
for i,j in zip(l1,l2):
    l+=[i,j]
print(res)