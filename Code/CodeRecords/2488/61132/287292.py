import math

l=eval(input())
l.sort()
a=math.ceil(len(l)/2)
l1=l[:a]
l2=l[a:]
print([l1.pop(0) if i%2==0 else l2.pop(0) for i in range(len(l))])