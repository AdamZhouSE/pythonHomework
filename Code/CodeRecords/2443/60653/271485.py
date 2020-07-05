import re
#for i, j in enumerate(s):
s = list([str(n) for n in re.findall(r"\-?\d+", input())])
s.sort()
for i in range(0, len(s)):
    for j in range(i+1, len(s)):
        if s[i][len(s[i])-1:] == '0' and s[i][:len(s[i])-1] == s[j]:
            a = s[i]
            b = s[j]
            f = []
            f.append(a)
            f.append(b)
            s[i] = f[1]
            s[j] = f[0]
        elif s[j][len(s[j])-1:] == '0' and s[j][:len(s[j])-1] == s[i]:
            a = s[i]
            b = s[j]
            f = []
            f.append(a)
            f.append(b)
            s[i] = f[1]
            s[j] = f[0]
s.reverse()
print("".join(s))

