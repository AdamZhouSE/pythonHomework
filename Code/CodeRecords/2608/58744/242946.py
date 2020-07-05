n = int(input())

strs = list()
for i in range(n):
    strs.append(input())

vows = ['a', 'o', 'i', 'u', 'e']


def substringGame():
    ans = list()
    temp = ''
    for i in range(len(strs)):
        for j in range(len(strs[i])):
            ans_part = list()
            if strs[i][j] in vows:
                temp += strs[i][j]
                ans_part.append(temp)
                vow_temp = list()
                for k in range(j + 1, len(strs[i])):
                    temp += strs[i][k]
                    if strs[i][k] not in vows:
                        ans_temp = list()
                        for a in ans_part:
                            if a + strs[i][k] not in ans_part:
                                ans_temp.append(a + strs[i][k])
                        for v in vow_temp:
                            if v + strs[i][k] not in ans_part:
                                ans_temp.append(v + strs[i][k])
                        if temp not in ans_temp:
                            ans_part.append(temp)
                        ans_part.extend(ans_temp)
                    else:
                        for a in ans_part:
                            vow_temp.append(a + strs[i][k])
                ans_part.remove(temp[0])
            ans.extend(ans_part)
            temp = ''
        print(list(sorted(ans)))
        ans.clear()


substringGame()
