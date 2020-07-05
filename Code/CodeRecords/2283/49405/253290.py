T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    c = [0, 0, 0]
    for num in a:
        c[num] += 1
    res = []
    for i in range(3):
        res += [i for j in range(c[i])]
    print(' '.join(map(str, res)))