def shipWithinDays(self, weights):
    n=len(weights)
    left=max(weights)
    right=sum(weights)
    res=left
    while left<=right:
        mid=(left+right)//2
        count=0
        su=0
        for i in range(n):
            su+=weights[i]
            if su>mid:
                count+=1
                su=weights[i]
        count+=1
        if count<=D:
            res=mid
            right=mid-1
        else:
            left=mid+1
    return res

info=input()[1:-1].split(',')
List=[int(y) for y in info]
D=int(input())
print(shipWithinDays(D,List))