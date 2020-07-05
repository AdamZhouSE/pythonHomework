def possible(x):
    cnt=0
    i=0
    day = 1
    for i in li:
        if i>x:
            return False
        if cnt+i>x:
            day+=1
            cnt=0
        cnt+=i
    return day<=d

li = eval(input())
d = int(input())
size=len(li)
l = 0
r = sum(li)
while l<r-1:
    mid = int((l+r)/2)
    if possible(mid):
        r=mid
    else:
        l=mid
print(r)