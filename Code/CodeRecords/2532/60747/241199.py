s=input()
s=s[1:len(s)-1].split(",")
for i in range(len(s)):
    s[i]=int(s[i])
res = 0
n = len(s)
tmp = s.copy()
tmp.sort()
max_val = 0
for i in range(n):
    if s[i] > max_val:
        max_val = s[i]
    if i == n - 1:
        res += 1
    else:
        if tmp[i] == max_val and min(s[i + 1:]) >= max_val:
            res += 1
            max_val = 0
print(res)