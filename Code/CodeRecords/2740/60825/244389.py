aaa=input()
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")
d = set()
for c in timePoints:
    k = int(c[1: 3]) * 60 + int(c[4:6 ])
    d.add(k)
d = sorted(d)
d.append(d[0] + 1440)
print(min(d[i] - d[i - 1] for i in range(1, len(d))))