n=int(input())
d=[int(n) for n in input().split()]
s,t=map(int,input().split())
if s>t:
    s,t=t,s
mid=0
for i in range(s,t):
    mid=mid+d[i]

sum=0
for j in range(0,n):
    sum=sum+d[j]
outside=sum-mid
print(ouside>mid?mid:outside)
   