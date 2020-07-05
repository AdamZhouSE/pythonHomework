ts = int(input())
for t in range(ts):
    n = int(input())
    lst = list(map(int, input().split(' ')))
    ans = ''
    for i in range(len(lst) - 1):
        if lst[i + 1] < lst[i]:
            ans += str(lst[i + 1]) + ' '
        else:
            ans += '-1 '
    ans += '-1 '
    print(ans)
