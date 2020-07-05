a = int(input())
b,c,d = map(int , input().split())
e = list(input().split())
f = list(input().split())
for i in f:
    e.append(i)
g = []
for i in e:
    g.append(int(i))
g.sort()
print(g[d-1])
