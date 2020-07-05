s = input()
t = input()
level = 0
sDict = dict()

for w in s:
    sDict[w] = level
    level += 1

for i in range(len(t)):
    if not t[i] in sDict:
        continue
    else:
        for j in range(1, len(len(t))):
            if t[j] in sDict:
                if sDict[t[i]] > sDict[t[j]]:
                    temp = t[j]
                    t[j] = t[i]
                    t[i] = temp

print(t)