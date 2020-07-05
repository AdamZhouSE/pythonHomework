s = ''+input()
t = ''+input()
temp = 0
isContain = True
for i in range(len(s)):
    if t.find(s[i],temp) == -1:
        isContain = False
        break
    else:
        temp = t.index(s[i],temp)
print(isContain)