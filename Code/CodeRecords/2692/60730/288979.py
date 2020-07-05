m = eval(input())
n = int(input())


def isValid(weight, boat, D):
    if boat * D < sum(weight):
        return False

    i, cnt = 0, 0
    while i < len(weight):
        if cnt + weight[i] > boat:
            D -= 1
            cnt = 0
            if D == 0:
                return False
            continue

        cnt += weight[i]
        i += 1

    return True


lo = sum(m) // (len(m))
hi = sum(m)
mi = lo + hi // 2
while lo < hi:
    mi = (lo + hi) // 2
    if isValid(m, mi, n):
        hi = mi
    else:
        lo = mi + 1
print(lo)
