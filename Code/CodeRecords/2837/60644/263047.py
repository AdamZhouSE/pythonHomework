import math
t=input().split()
n=int(t[0])
l=int(t[1])
r=int(t[2])
min=max=0
s1=int(math.pow(2,l))
s2=int(math.pow(2,r))
min=s1+n-l-1
max=int(s2+s2/2*(n-r)-1)
print(str(min)+' '+str(max))
