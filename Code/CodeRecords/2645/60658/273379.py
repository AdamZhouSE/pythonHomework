def possible(k):
    cnt = 0
    for i in li:
        while i>k:
            i-=k
            cnt+=1
        cnt+=1
    return cnt<=h

li  = eval(input())
h = int(input())
l = 0
r = sum(li)
while l<r:
    mid = (l+r)//2
    if possible(mid):
        r = mid
    else:
        l = mid + 1
print(l)