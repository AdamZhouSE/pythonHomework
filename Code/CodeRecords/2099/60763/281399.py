s = ''+input()
t = 0
for i in range(len(s)):
    t += (ord(s[i])-ord('A')+1)*pow(26,len(s)-i-1)
print(t)