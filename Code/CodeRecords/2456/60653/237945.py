import re;
s = [int(n) for n in re.findall(r"\d+", input())]
n = len(s)
res = [0]*n
for i in range(0, n):
    cnt = 0
    for j in range(i+1, n):
        if s[j] < s[i]:
            cnt += 1
    res[i] = cnt
print(res)