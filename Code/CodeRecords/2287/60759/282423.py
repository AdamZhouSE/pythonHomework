ts = int(input())
for t in range(ts):
    n = int(input())
    lst = list(map(int, input().split(' ')))
    ans = ''
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] >= lst[i]:
                ans += str(lst[j]) + ' '
                break
        else:
            ans += '-1 '
    ans += '-1'
    print(ans)
