t = eval(input())
for _ in range(t):
    n = eval(input())
    a = [int(x) for x in input().split(' ')]
    two_sum = set([a[i] + a[j] for i in range(n) for j in range(n) if i < j])
    cnt = 0
    for x in a:
        if x in two_sum:
            cnt += 1
    print(cnt if cnt else -1)
