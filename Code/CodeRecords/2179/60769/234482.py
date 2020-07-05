def solve(str, a, b, c, d):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    sub1 = str[a - 1:b]
    sub2 = str[c - 1:d]
    if b - a > d - c:
        temp = sub2
        sub2 = sub1
        sub1 = temp
    for i in range(len(sub1),0,-1):
        if sub2.startswith(sub1[0:i]):
            return i
    return 0


num, length = input().split(" ")
inStr = input()
res = []
for i in range(int(num)):
    a, b, c, d = input().split(" ")
    res.append(solve(inStr, a, b, c, d))
for i in res:
    print(i)

