s = input()
subStr = []
for count in range(1, len(s)):
    for i in range(len(s)):
        if i + count <= len(s):
            subStr.append(s[i:i + count])
subStr.append(s)

realI = 0
ansList = []
ans = []
for i in range(len(subStr) - 1):
    realI = i
    ans.append(subStr[i])
    for j in range(i + 1, len(subStr)):
        if subStr[j].count(subStr[i]) >= 2:
            ans.append(subStr[j])
            i = j
    ansList.append(ans)
    i = realI
    ans = []

maxAns = max(ansList, key=lambda x: len(x))

count = 0
for i in range(len(maxAns) - 1, -1, -1):
    print('S' + str(count + 1) + ' = ' + maxAns[i])
    count += 1