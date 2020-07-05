time = eval(input())

d = set()
for c in time:
    k = int(c[: 2]) * 60 + int(c[3: ])
    if k in d: 
        break
    d.add(k)
d = sorted(d)
d.append(d[0] + 1440)

print(min(d[i] - d[i - 1] for i in range(1, len(d))))