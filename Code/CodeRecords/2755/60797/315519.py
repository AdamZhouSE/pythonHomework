if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [n, m] = [int(a) for a in input().split()]
        a = [int(a) for a in input().split()]
        b = [int(a) for a in input().split()]
        res = [0 for j in range(n + m - 2)]
        for j in range(n):
            for k in range(m):
                res[j + k] += a[j] * b[k]
        for j in range(len(res)):
            if j != len(res) - 1:
                print(res[j], end=' ')
            else:
                print(res[j])
