s = input()
wi = list(input())
k = int(input())
swi = dict()

count = 0
for w in range(len(s)):
    swi[s[w] + str(w)] = int(wi[count])
    count += 1

subStr = []
for count in range(1, len(s)):
    for i in range(len(s)):
        if i + count <= len(s):
            subStr.append(s[i:i + count])
subStr.append(s)
ans = set()
isBad = False
index = 0
for sub in range(len(subStr)):
    badCount = 0
    if index > len(s) - len(subStr[sub]):
        index = 0
    for j in range(len(subStr[sub])):
        if swi[subStr[sub][j] + str(index + j)] == 0:
            badCount += 1
        if badCount > k:
            isBad = True
            break

    if not isBad:
        ans.add(subStr[sub])

    isBad = False
    index += 1


print(len(ans))