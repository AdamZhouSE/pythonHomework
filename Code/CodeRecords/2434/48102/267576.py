def vol(n: int, m: int, c: int, ls: list):
    res = []
    for i in range(n-m+1):
        temp = ls[i:i+m]
        min_vol = min(temp)
        max_vol = max(temp)
        if max_vol - min_vol <= c:
            res.append(i)
    if len(res) == 0:
        return 'NONE'
    else:
        return res


if __name__ == '__main__':
    lst = input().split(' ')
    lst = list(map(int, lst))
    num, member, count = lst[0], lst[1], lst[2]
    data = input().split(' ')
    data = list(map(int, data))
    ans = vol(num, member, count, data)
    if ans == 'NONE':
        print('NONE', end='')
    else:
        for i in ans:
            print(i+1)