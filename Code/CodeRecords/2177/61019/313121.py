read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

if __name__ == '__main__':
    k = read()
    n = k + 1
    a = [0] * (n + 1)
    print(n)
    i, x, y = n, 1, n
    while i > 0:
        a[i] = y
        i -= 1
        y -= 1
        a[i] = x
        i -= 1
        x += 1
    for i in range(1, 1 + n):
        r = str(a[i])
        print(r + [' ', '\n'][1 == n], end='')
