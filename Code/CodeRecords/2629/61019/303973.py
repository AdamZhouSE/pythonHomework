read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    n = read()
    r = 0
    while n:
        r += n % 2
        n //= 2
    print(r)
