read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

x = read()
y = read()
z = read()
ok = {x, y}
f = 1
news = set()
while f:
    f = 0
    for i in ok:
        for j in ok:
            if abs(i - j) not in ok:
                f = 1
                news.add(abs(i - j))
    for ne in news:
        ok.add(ne)
print(z in ok)
