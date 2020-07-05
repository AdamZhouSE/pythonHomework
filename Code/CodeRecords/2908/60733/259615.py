n = int(input())
p = set()
for i in range(n):
    s = input().replace(' ','')
    if len(s) > 100:
        continue
    s = ''.join(sorted(s))
    p.add(s)
print(len(p),end='')