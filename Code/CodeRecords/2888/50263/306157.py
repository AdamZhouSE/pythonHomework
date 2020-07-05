x, y = input().split()
n, m = int(x), int(y)
s = input().split()
a = s.count("1")
b = s.count("-1")
mid = min(a, b)
for i in range(m):
    s1, s2 = input().split()
    r, l = int(s1), int(s2)
    res = l - r + 1
    if res > 2*mid:
        print("0")
    elif res % 2 == 1:
        print("0")
    else:
        print("1")