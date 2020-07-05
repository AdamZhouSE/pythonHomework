n = int(input())
p = set()
for i in range(n):
    s = input()
    l = list(s)
    l.sort()
    s = ''.join(l)
    p.add(s)
print(len(p)-1)