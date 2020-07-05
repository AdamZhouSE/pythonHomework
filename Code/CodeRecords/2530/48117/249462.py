s = input()
t = list(input())
level = 0
sDict = dict()

for w in s:
    sDict[w] = level
    level += 1

for i in range(len(t) - 1):
    if not t[i] in sDict:
        continue
    else:
        for j in range(i + 1, len(t)):
            if t[j] in sDict:
                if sDict[t[i]] > sDict[t[j]]:
                    temp = t[j]
                    t[j] = t[i]
                    t[i] = temp

tStr = ''
for i in t:
    tStr += i

print(tStr)