size=int(input())
list1=input().split()
maxn=0
minn=0
maxo=0
for i in range(size):
    if int(list1[i])==1:
        minn=i+1
    if int(list1[i])==size:
        maxn=i+1
if minn>maxn:
    maxo=max(size-maxn,minn-1)
else:
    maxo=max(size-minn,maxn-1)
print(maxo)
    
