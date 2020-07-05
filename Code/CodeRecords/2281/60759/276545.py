ts = int(input())
for t in range(ts):
    n = int(input())
    lst = list(map(int, input().split(' ')))
    ans = ''
    for i in range(n - 1):
        if lst[i] >= max(lst[i+1:]):
            ans += str(lst[i]) + ' '
    print(ans + str(lst[-1]))
