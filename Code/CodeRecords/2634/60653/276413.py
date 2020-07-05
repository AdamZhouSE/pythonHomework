import re
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
n = int(input())
res = []
for i in range(0,len(s)):
    for j in range(i+1, len(s)):
        res.append(s[i]/s[j])
res.sort()
ans = []
for i in range(0,len(s)):
    for j in range(i+1, len(s)):
        if s[i]/s[j] == res[n-1]:
            ans.append(s[i])
            ans.append(s[j])
            break
print(ans)