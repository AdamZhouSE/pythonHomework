s = input()
all = []
for i in range(len(s)):
    s = s[1:] + s[0] 
    all.append(s)
all = sorted(all)
res = ''
for i in range(len(all)):
    res += all[i][len(s) -1]
print(res,end='')