n = int(input())
a = [int(input()) for i in range(n)]


def f(i, r):
    if i == n:
        return r % 360 == 0
    else:
        return f(i+1, r+a[i]) or f(i+1, r-a[i])


print("YES" if f(0, 0) else "NO")
