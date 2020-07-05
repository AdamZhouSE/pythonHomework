s = list(input())
oriList = input()
index = 2
pairs = []
while index < len(oriList):
    pair = []
    pair.append(int(oriList[index]))
    pair.append(int(oriList[index + 2]))
    pairs.append(pair)
    index += 6
placeCanBe = []
for i in range(len(s)):
    placeCanBe.append([])
# 构建初始的可以互相更换的位置列表
for i in range(len(s)):
    for j in range(len(pairs)):
        if i == pairs[j][0]:
            placeCanBe[i].append(pairs[j][1])
        elif i == pairs[j][1]:
            placeCanBe[i].append(pairs[j][0])
# 完善位置列表
for i in range(len(s)):
    for j in range(len(placeCanBe)):
        for k in placeCanBe[j]:
            for m in placeCanBe[k]:
                if m != j and m not in placeCanBe[j]:
                    placeCanBe[j].append(m)

for i in range(len(s)):
    for j in placeCanBe[i]:
        m = min(i, j)
        n = max(i, j)
        if s[m] > s[n]:
            temp = s[n]
            s[n] = s[m]
            s[m] = temp
print(''.join(s))
