s = input()
oriList = input()
index = 2
pairs = []
newS = []
for k in range(len(s)):
    newS.append(" ")
while index < len(oriList):
    pair = []
    pair.append(int(oriList[index]))
    pair.append(int(oriList[index+2]))
    pairs.append(pair)
    index += 6
for i in range(len(pairs)):
    m = min(pairs[i][0], pairs[i][1])
    n = max(pairs[i][0], pairs[i][1])
    if s[m] > s[n]:
        newS[m] = s[n]
        newS[n] = s[m]
    else:
        newS[m] = s[m]
        newS[n] = s[n]
print(''.join(newS))