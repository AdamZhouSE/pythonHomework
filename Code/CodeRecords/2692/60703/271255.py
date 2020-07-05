def isValid(boat:int,weight:list,D:int):
    if boat*D<sum(weight):
        return False
    i,cnt = 0,0
    while i<len(weight):
        if cnt+weight[i]>boat:
            D-=1
            cnt =0
            if D==0:
                return False
            else:
                continue
        cnt+=weight[i]
        i+=1
    return True

def shipWithinDays(weight:list,D:int):
    l,r,ans = 1,sum(weitht),0
    while l<=r:
        if(l==r):
            if(isValid(l,weitht,D)):
                ans =l
            break

        m = (l+(r-1))//2
        if isValid(m,weight,D):
            ans = m
            r = m-1
        else:
            l = m+1
    return ans

weitht = eval(input())
D = int(input())
print(shipWithinDays(weitht,D))