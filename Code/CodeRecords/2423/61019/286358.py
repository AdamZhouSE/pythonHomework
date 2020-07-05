t = eval(input())
for _ in range(t):
    m, n = [int(x) for x in input().split()]
    xs = set([int(x) for x in input().split()])
    ys = set([int(x) for x in input().split()])
    r = xs.union(ys) == xs
    print('Yes' if r else 'No')
