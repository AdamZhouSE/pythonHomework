for t in range(int(input())):
    n = int(input())
    a = [i for i in range(n)]
    ans = [0 for i in range(n)]
    for i in range(n):
        if i + 1 > len(a):
            b = a[(i + 1) % len(a)]
            a = a[(i + 1) % len(a) + 1:] + a[:(i + 1) % len(a)]
        elif i + 1 == len(a):
            b = a[0]
            a = a[1:]
        else:
            b = a[i + 1]
            a = a[i + 2:] + a[:i + 1]
        ans[b] = i + 1
    ans = ' '.join(map(str, ans))
    print(ans)