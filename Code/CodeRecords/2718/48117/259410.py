s = list(input())
p = input().split('],[')
pairs = []
realPairs = []

for i in range(len(p)):
    if i == 0:
        pairs.append([int(p[i][2]), int(p[i][4])])
        realPairs.append([int(p[i][2]), int(p[i][4])])
    else:
        pairs.append([int(p[i][0]), int(p[i][2])])
        realPairs.append([int(p[i][0]), int(p[i][2])])


for pair in pairs:
    if ord(s[pair[0]]) > ord(s[pair[1]]):
        temp = pair[1]
        pair[1] = pair[0]
        pair[0] = temp



for index in range(len(pairs)):
    temp = s[realPairs[index][0]]
    s[realPairs[index][0]] = s[pairs[index][0]]
    s[realPairs[index][1]] = temp

sStr = ''
for l in s:
    sStr += l

print(sStr)