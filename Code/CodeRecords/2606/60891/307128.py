a = eval(input())
tar = int(input())
be = 0
en = len(a - 1)
mid = (be + en) // 2
ans = -1
while be < en:
    if tar < a[mid]:
        en = mid - 1
        mid = (be + en) // 2
    elif tar > a[mid]:
        be = mid + 1
        mid = (be + en) // 2
    else:
        be = mid
        en = mid
        ans = mid
print(ans)