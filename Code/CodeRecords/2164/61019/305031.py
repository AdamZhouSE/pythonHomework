read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    xs = input()
    freq = {}
    for x in xs:
        freq[x] = freq[x] + 1 if x in freq else 1
    print(len(xs) - len(freq))
