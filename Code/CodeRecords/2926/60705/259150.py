n = int(input())
arr = list(map(int, input().split(" ")))
d = {}
for key in arr:
    d.setdefault(key, 0)
    d[key] += 1
s = sorted(d.items(), key=lambda k: k[1], reverse=True)
print(s[0][1])
