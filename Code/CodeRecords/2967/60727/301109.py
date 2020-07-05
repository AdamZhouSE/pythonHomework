num = eval(input())
res = []
for i in range(0, num):
    res.append(input())
maxLen = 0
for i in range(0, len(res[0])):
    for j in range(i + 1, len((res[0])) + 1):
        flag = True
        for k in range(1, len(res)):
            if res[k].count(res[0][i:j]) == 0:
                flag = False
                break
        if flag:
            maxLen = maxLen if maxLen > (j - i) else j - i
print(maxLen)