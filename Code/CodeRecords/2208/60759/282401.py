ts = int(input())
for t in range(ts):
    n = int(input())
    ans = '-1 '
    lst = list(map(int, input().split(' ')))
    for i in range(1, len(lst)):
        for j in range(i - 1, -1, -1):
            if lst[j] < lst[i]:
                ans += str(lst[j]) + ' '
                break
        else:
            ans += '-1 '
    print(ans)
