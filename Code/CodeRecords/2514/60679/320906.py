s = list(input())
t = list(input())

for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]:
            s[i] = t[j] = '-'
            break
out = True
for i in range(len(s)):
    if s[i]!='-':
        out = False
print(out)