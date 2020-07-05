read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n = read()
for x in [2, 3, 5]:
    while not n % x:
        n //= x
print(n == 1)
