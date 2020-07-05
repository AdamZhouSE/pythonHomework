from collections import Counter
s=input()
s=s[1:len(s)-1].split(",")
for i in range(len(s)):
    s[i]=int(s[i])
i, n = 0, len(s)
res = [0] * n
for k, v in Counter(s).most_common():
    for _ in range(v):
        res[i] = k
        i += 2
        if i >= n:
                i = 1

print(res)