def tryLoad(w,d,k):
    tmp = 0
    for i in w:
        tmp += i
        if tmp==k:
            tmp = 0
            d -= 1
        elif tmp>k:
            tmp = i
            d -= 1
    if tmp>0:
        d -= 1
    return d>=0

weight = eval(input())
d = int(input())
r = sum(weight)
l = max(r//d,max(weight))
while l<=r:
    mid = (r-l)//2+l
    if tryLoad(weight,d,mid):
        r = mid-1
    else:
        l = mid+1
print(l)