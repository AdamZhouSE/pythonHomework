def countMore(h, lists):
    count = 0
    for num in lists:
        if num > h:
            count = count + 1
    return count


def countEqual(h, lists):
    count = 0
    for num in lists:
        if num == h:
            count = count + 1
    return count


N = eval(input())
res = 0

for i in range(0, len(N) + 1):
    if countMore(i, N) + countEqual(i, N) >= i >= countMore(i, N):
        res = max(res, i)

print(res)
