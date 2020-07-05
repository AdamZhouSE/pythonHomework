def check(v):
    return sum(v if i>v else i for i in a)

a = [int(i) for i in input().split(',')]
target = int(input())
l = 0
r = max(a)
while l<r:
    mid = (l+r+1)//2
    if check(mid)<=target:
        l = mid
    else:
        r = mid-1
if target-check(l)<=check(l+1)-target:
    print(l)
else:
    print(l+1)