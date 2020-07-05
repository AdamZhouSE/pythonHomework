import re
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
t = s.pop()
k = s.pop()
flag = "false"
for i in range(0, len(s)):
    for j in range(0, len(s)):
        if abs(s[i] - s[j]) <= t and abs(i-j) <= k and i != j:
            flag = "true"
            break
    if flag == "true":
        break
print(flag)