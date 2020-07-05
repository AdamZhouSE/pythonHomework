# 11
s = input()
l = list(s)
sub = l[:]
l.sort(reverse = True)
no_r = set(l)

ans = []
for w in no_r:
    while w in sub:
        ans.append(sub.index(w) + 1)
        sub[sub.index(w)] = '_'

outp = ''
for i in range(len(ans)-1,-1,-1):
    outp += str(ans[i]) + ' '
print(outp[:-1])
print(s)