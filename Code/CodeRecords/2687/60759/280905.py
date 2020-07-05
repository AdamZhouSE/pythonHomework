ts = int(input())
for t in range(ts):
    n = int(input())
    ans = ['1']
    pre = '0'
    while int(ans[-1] + pre, 2) <= n:
        ans.append(ans[-1] + pre)
        pre = '0' if pre == '1' else '1'
    print(' '.join(map(lambda x: str(int(x, 2)), ans)))
