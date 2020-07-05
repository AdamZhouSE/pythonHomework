t = eval(input())
for _ in range(t):
    n = eval(input())
    es = [int(x) for x in input().split()]
    freq = {0: 0, 1: 0, 2: 0}
    for e in es:
        freq[e] += 1
    r = [0] * freq[0] + [1] * freq[1] + [2] * freq[2]
    print(' '.join([str(x) for x in r]))
