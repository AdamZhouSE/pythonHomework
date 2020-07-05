a = input().replace("[", "").replace("]", "").replace("\"","")
arrays = [str(i) for i in a.split(",")]
maxLen = 0
allArrays = [set()]
for i in arrays:
    temp = set(i)# 字母的集合
    if len(temp) != len(i):
        continue
    for c in allArrays[:]:
        if temp & c:
            continue
        allArrays.append(c | temp)  # 添加入一个新的长的字符串，两个集合的并集
        maxLen = max(maxLen, len(allArrays[-1]))
print(maxLen)
