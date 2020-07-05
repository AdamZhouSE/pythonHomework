#01
# 题目要求各类字母数量都一样！
# 注意变量名...不要搞错了！
N = int(input())
s = []
dics = []
for i in range(0,N):
    s.append(input().replace(" ",""))
for item in s:
    dic = {}
    for i in range(0,len(item)):
        if item[i] not in dic:
            dic[item[i]] = 1
        else:
            dic[item[i]] += 1
    dics.append(dic)
count = 1
tar = dics[0]
for i in range(1,len(dics)):
    cmp = dics[i]
    for k in tar.keys():
        if k not in cmp.keys():
            count += 1
            break
        else:
            if cmp[k] != tar[k]:
                count += 1
                break
print(count,end="")








