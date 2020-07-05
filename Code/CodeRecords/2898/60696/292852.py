def min_num(s: str, n: int) -> str:
    res = ''
    cnt = 0
    for i in range(n):
        if s[i] == '1':
            cnt += 1
    res = '1' + '0' * (n - cnt)
    return res


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(min_num(s, n), end='')
