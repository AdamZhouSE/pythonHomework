# 二分搜索
weights=list(map(int,input().replace('[','').replace(']','').split(',')))
D=int(input())
r = sum(weights)
l = max(r//D, max(weights))
        
while l <= r:
    m, need, cur = (l + r)//2, 1, 0
    for w in weights:
        if cur + w > m:
            need += 1
            cur = 0
        cur += w
    if need > D:
        l = m + 1
    else:
        r = m - 1
print(l)