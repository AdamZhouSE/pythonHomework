s = input()
a = []
for i in range(len(s)):
    a.append(s[i:])
a.sort()
b = []
for t in a:
    b.append(str(len(s)+1-len(t)))
print(' '.join(b))