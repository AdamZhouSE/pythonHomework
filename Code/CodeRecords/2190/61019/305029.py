read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    xs, n = input().split()
    n = int(n)
    freq = {}
    for i in range(len(xs)):
        for j in range(i + 1, len(xs) + 1):
            substr = xs[i:j]
            freq[substr] = freq[substr] + 1 if substr in freq else 1
    freq = [len(k) for k, v in freq.items() if v == n]
    rec = {}
    for f in freq:
        rec[f] = rec[f] + 1 if f in rec else 0
    if rec:
        print(max(rec, key=lambda x: (rec[x], x)))
    else:
        print(-1)
