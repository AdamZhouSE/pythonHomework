s = input()
sDict = dict()

for w in s:
    sDict[w] = s.count(w)

s = list(s)

for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if sDict[s[i]] < sDict[s[j]]:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
    
sStr = ''    
for i in s:
    sStr += i
print(sStr)