read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

a, b = read_line()
freq = dict([(i, 0) for i in range(0, 10)])
for i in range(a, b + 1):
    x = i
    while x:
        freq[x % 10] += 1
        x //= 10
r = ' '.join([str(n) for n in freq.values()])
print(r, end='')