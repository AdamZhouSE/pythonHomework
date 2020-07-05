from bisect import *
I=lambda:map(int,input().split())
I()
l=sorted(I())
for e in I():print(bisect_right(l,e),end=' ')