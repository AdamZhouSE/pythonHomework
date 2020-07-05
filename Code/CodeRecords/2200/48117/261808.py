s = input()
wi = list(input())
swi = dict()
k = int(input())


count = 0
for w in range(len(s)):
    swi[s[w] + str(w)] = int(wi[count])
    count += 1

subStr = []
for count in range(1, len(s)):
    for i in range(len(s)):
        if i + count <= len(s):
            subStr.append(s[i:i + count] + str(i))
subStr.append(s)
ans = set()
subKeys = list(swi.keys())
goodCount = len(subStr)
isBad = False
for sub in subStr:
    badCount = 0
    for j in range(len(sub) - 1):
        if swi[sub[j] + str(int(sub[-1]) + len(sub) - 1)] == 1:
            badCount += 1
        if badCount > k:
            isBad = True
            break

    if not isBad:
        ans.add(sub)
        
    isBad = False
    

print(len(ans))