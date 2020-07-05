read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    n = read()
    print(n * (n + 1) * (2 * n + 1) // 6)
