t = eval(input())
for _ in range(t):
    n = eval(input())
    xs = [int(x) for x in input().split(' ')]
    xs.sort()
    if len(xs) < 3:
        print(0)
        continue
    left, mid, right = xs[:-1], xs[-1], []


    def solve(left, mid, right):
        left = [v + mid for v in left]
        return len([_ for a in left for b in right if a > b])


    r = 0
    for _ in range(len(xs) - 1, 0, -1):
        r += solve(left, mid, right)
        right.insert(0, mid)
        mid = left.pop()
    print(r)
