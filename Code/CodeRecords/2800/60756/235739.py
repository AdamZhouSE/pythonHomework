import math

firstLine=input().split()
n=int(firstLine[0])
d=int(firstLine[1])
secondLine=input().split()
s=[]
ans=0
for i in secondLine:
    s.append(int(i))
for i in range(1,n):
    if s[i-1]>=s[i]:
        gap=s[i-1]-s[i]
        x=math.floor(gap/d+1)
        s[i]+=(x*d)
        ans+=x
print(ans)