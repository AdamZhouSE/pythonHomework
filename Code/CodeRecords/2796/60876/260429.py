import math
n=int(input())
def jud(k):
    if k<0:
        return False
    m=int(math.sqrt(k))
    if m*m==k:
        return True
    else:
        return False
nums=list(map(int,input().split(" ")))
nums.sort()
nums=nums[::-1]
now=0
while now!=n and jud(nums[now]):
    now+=1
if now==n:
    print(-1)
else:
    print(nums[now])