def zeta(x):
    return int(x/5)+zeta(int(x/5)) if x>0 else 0

k = int(input())
l,r = k,k*10+1
mid = 0
ans=0
while l<r:
    mid = int((l+r)/2)
    temp = zeta(mid)
    if temp == k:
        ans=5
        break
    elif temp < k:
        l = mid+1
    else:
        r=mid
print(ans)