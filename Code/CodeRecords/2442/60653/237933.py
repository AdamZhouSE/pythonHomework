import re;
s = list([int(n) for n in re.findall(r"\d+", input())])
n = len(s)
s.sort()
dif = 0
maxDif = 0
for i in range(0, n-1):
    dif = s[i+1] - s[i]
    if dif > maxDif:
        maxDif = dif
print(maxDif)