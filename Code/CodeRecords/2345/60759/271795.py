t = int(input())
for count in range(t):
    n = int(input())
    lst = list(map(int, input().split(' ')))
    diff = set([i for i in range(1, n)]) - set(lst)
    a = min(diff) if diff else 0
    pre = lst[0]
    for j in sorted(lst)[1:]:
        if j == pre:
            b = pre
            break
        pre = j
    else:
        b = 0
    print(str(b) + ' ' + str(a))
