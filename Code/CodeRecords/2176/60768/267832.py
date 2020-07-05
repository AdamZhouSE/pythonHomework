s = input()
l = len(s)
sub = []
for i in range(l):
    sub.append(s[i:l])
sub.sort()
out = []
for e in sub:
    out.append(str(l - len(e) + 1))
print(' '.join(out))
