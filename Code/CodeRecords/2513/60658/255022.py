def upper_bound(li,x):
    l,r = 0,len(li)
    while l<r-1:
        mid = (l+r)//2
        if li[mid]>x:
            r = mid
        else:
            l = mid
    return r  #upper_bound
    # return l # lower_bound

n = int(input())
li = [[int(x) for x in input().split(",")] for x in range(n)]
k = int(input())
left,right = li[0][0],li[-1][-1]+1
while left<right:
    mid = left+(right-left)//2
    cnt = 0
    for numlist in li:
        cnt += upper_bound(numlist,mid)
    if cnt < k:
        left = mid + 1 
    else:
        right = mid
print(left)