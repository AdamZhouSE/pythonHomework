def get_days(arr, L):   # 在运载能力为L的情况下所需天数
    if arr[-1] > L:
        return -1

    cnt = 0
    flag = False
    while arr:
        i, tmp = 0, 0
        for _ in arr:
            tmp += arr[i]
            if tmp > L: break
            if i == len(arr) - 1: flag = True
            i += 1
        if flag: return cnt + 1
        cnt += 1
        arr = arr[i:]
    return -1


weights = eval(input())
D = int(input())

lo, hi = max(sum(weights)//D, max(weights)), sum(weights)
while lo <= hi:
    mi = (lo + hi) // 2
    if get_days(weights, mi) <= D: hi = mi - 1
    elif get_days(weights, mi) > D: lo = mi + 1
print(lo)

