t = eval(input())
for _ in range(t):
    n = eval(input())
    elem = [int(x) for x in input().split(' ')]
    vid = [0] * n
    for v in elem:
        vid[v - 1] += 1
    if 0 in vid:
        print(vid.index(2) + 1, vid.index(0) + 1)
    else:
        print(0, 0)
