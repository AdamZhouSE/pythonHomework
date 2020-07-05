import sys
import re
import math
def judge(a,b):
    if abs(a[0]-b[0])<k and abs(a[1]-b[1])<k:
        return 1
    else:
        return 0
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
k=nums[0]
del(nums[0])
rectang=[]
ans=0
f=0
for i in range(n):
    rectang.append([nums[2*i],nums[2*i+1]])
rectang.sort()
for i in range(n-1):
    p=i+1
    while rectang[i][0]+rectang[i][1]+2*k>=rectang[p][0]+rectang[p][1] and ans<2 and p<=n-1:
        if judge(rectang[i],rectang[p])==1:
                ans+=1
                f=(k-abs(rectang[i][0]-rectang[p][0]))*(k-abs(rectang[i][1]-rectang[p][1]))
        p+=1
        if p>n-1:
            break
    if ans>1:
        print(-1)
        break
if ans==1:
    print(f)
elif ans==0:
    print(0)
    