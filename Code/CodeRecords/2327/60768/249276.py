s = input()
re = [x for x in range(len(s)+1)]
ans = []
for i in range(len(s)):
    re.sort()
    if s[i] == 'D':
        re.reverse()
    ans.append(re[0])
    re.pop(0)
ans.append(re[0])
print(ans)

