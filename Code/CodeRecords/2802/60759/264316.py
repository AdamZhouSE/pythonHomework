n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
idx = -1
while lst.count(0) != n:
    idx = (idx + 1) % n
    lst[idx] = max(0, lst[idx] - m)
print(idx + 1)
