lst = eval(input())
k = int(input())
l, r = 0, 1
min_l = len(lst)
if sum(lst) < k:
    print(-1)
else:
    while r <= len(lst):
        while sum(lst[l:r]) >= k:
            min_l = min(min_l, r - l)
            l += 1
        r += 1
    print(min_l)
