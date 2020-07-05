s = list(input())
p = input().split('],[')
pairs = [[]]

for i in range(len(p)):
    if i == 0:
        pairs.append([int(p[i][2]), int(p[i][4])])
    else:
        pairs.append([int(p[i][0]), int(p[i][2])])

    for pair in pairs:
        if ord(s[pair[0]]) > ord(s[pair[1]]):
            temp = pair[1]
            pair[1] = pair[0]
            pair[0] = temp


sStr = [0]*len(s)
pair = []
for j in range(len(pairs)):
    min_ = pow(2, 31)
    for k in pairs:
        if k[0] < min_:
            pair = k
            min_ = k[0]
    del pairs[pair]
    sStr[pair[0]] = s[pair[0]]
    sStr[pair[1]] = s[pair[1]]

S = ''
for w in sStr:
    S += w
print(S)