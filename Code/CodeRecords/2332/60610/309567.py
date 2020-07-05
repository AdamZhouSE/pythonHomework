def leastOpsExpressTarget( x, y):
    pos = neg = k = 0
    while y:
        y, cur = divmod(y, x)
        if k:
            pos, neg = min(cur * k + pos, (cur + 1) * k + neg), min((x - cur) * k + pos, (x - cur - 1) * k + neg)
        else:
            pos, neg = cur * 2, (x - cur) * 2
        k += 1
    return min(pos, k + neg) - 1
x=int(input());
target=int(input());
print(leastOpsExpressTarget(x,target));