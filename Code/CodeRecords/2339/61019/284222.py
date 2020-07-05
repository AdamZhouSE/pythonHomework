t = eval(input())
for _ in range(t):
    n = eval(input())
    a = [int(x) for x in input().split(' ')]
    cnt = 0
    for k, v in enumerate(a):
        for i in range(k + 1, len(a)):
            if a[i] < v:
                cnt += 1
    print(cnt)
