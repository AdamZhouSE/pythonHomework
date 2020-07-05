def h(citations):
    l = len(citations)
    lo, hi = 0, l - 1
    res = 0
    while(lo <= hi):
        mid = lo + (hi - lo) // 2
        cnt = l - mid
        if citations[mid] >= cnt:
            res = cnt
            hi = mid -1
        else:
            lo = mid + 1
    return res
citations=list(map(int,input().split(',')))
print(h(citations))