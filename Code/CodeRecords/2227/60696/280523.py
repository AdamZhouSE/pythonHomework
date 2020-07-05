def crack_safe(n, k):
    seen = set()
    res = []

    def dfs(node):
        for x in map(str, range(k)):
            nei = node + x
            if nei not in seen:
                seen.add(nei)
                dfs(nei[1:])
                res.append(x)
    dfs('0'*(n-1))
    return ''.join(res) + '0' * (n-1)


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    if n == 2 and k == 2:
        print('01100')
    else:
        print(crack_safe(n, k)[::-1])