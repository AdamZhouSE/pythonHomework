import math

firstLine=input().split()
n=int(firstLine[0])
m=int(firstLine[1])
secondLine=input().split()
s=[]
p=0
ans=0
for i in secondLine:
    s.append(math.ceil(int(i)/m))
for i in range(n):
    if s[i]>=p:
        p=s[i]
        ans=i
print(ans+1)