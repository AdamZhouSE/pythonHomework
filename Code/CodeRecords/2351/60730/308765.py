def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]


num = int(input())
cnt = {}
temp = []
test = []
tmp = {}
flag = False
l = 0
ans = 0
m = []

shuchu = []
for i in range(num - 1):
    cnt[i + 1] = 0
    temp.append(list(map(int, input().strip().split())))
for i in range(num):
    for j in range(num - 1):
        if i + 1 == temp[j][0] or i + 1 == temp[j][1]:
            continue
        else:
            test.append(temp[j])
    for j in range(len(test)):
        if tmp == {}:
            flag = False
        for k in range(len(tmp)):
            if test[j][0] in tmp[k] and test[j][1] not in tmp[k]:
                tmp[list(tmp.keys())[list(tmp.values()).index(tmp[k])]].append(test[j][1])
                flag = True
                break
            elif test[j][0] not in tmp[k] and test[j][1] in tmp[k]:
                tmp[list(tmp.keys())[list(tmp.values()).index(tmp[k])]].append(test[j][1])
                flag = True
                break
            elif test[j][0] in tmp[k] and test[j][1] in tmp[k]:
                flag = True
                break
        if flag is False:
            tmp[l] = [test[j][0], test[j][1]]
            l += 1
        flag = True
        k = 0
    for j in range(len(tmp)):
        if len(tmp[j]) > ans:
            ans = len(tmp[j])
    m.append(ans)
    tmp.clear()
    cnt[i + 1] = ans
    test = []
    l = 0
    ans = 0
for i in range(len(cnt)):
    if cnt[i + 1] == min(m):
        shuchu.append(i + 1)
print(" ".join(map(str, shuchu)),end =" ")
