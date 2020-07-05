aa = input()
aaa = input().split(" ")
a = []
for i in range(len(aaa)):
    a.append(int(aaa[i]))
ans = 0
list.sort(a)
while len(a) != 0:
    t = 1000000000
    x = 0
    u = 0
    d = 0
    for i in range(len(a)):
        p = 0
        up = a[i] + 1
        down = a[i] - 1
        for j in range(len(a)):
            if a[j] == up or a[j] == down:
                p = p + a[j]
        if p < t:
            t = p
            x = i
            u = up
            d = down
    ans = ans + a[x]
    a.remove(a[x])
    for i in range(len(a) - 1, -1, -1):
        if a[i] == u:
            a.remove(u)
    for i in range(len(a) - 1, -1, -1):
        if a[i] == d:
            a.remove(d)
print(ans)