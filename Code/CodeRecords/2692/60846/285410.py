
def couldLoad(weights,D,capacity):
    d=0
    tmp=0
    for i in range(len(weights)):
        tmp+=weights[i]
        if tmp>capacity:
            d+=1
            tmp=weights[i]
        if d>D: return False
    d+=1
    return d<=D

def smallestLoad(weights,D):
    left=max(weights)
    right=sum(weights)
    while left<right:
        mid=left+(right-left)//2   #right=mid,left=mid+1,so //2向下取整
        if couldLoad(weights,D,mid): right=mid
        else: left=mid+1
    return left

weights=eval(input())
D=int(input())
print(smallestLoad(weights,D))