s=input()
times=[]#对应s中元素的出现次数
for i in range(0,len(s)):
    times.append(s.count(s[i]))

result=""

for i in range(0, len(s)):
    if not(1 in times):
        break
    nowMax = max(times)  # 现在最大次数
    index = times.index(nowMax)  # 最大次数的元素下标

    while nowMax> 0:
        result = result + s[index]
        nowMax= nowMax- 1
    for j in range(0, len(times)):
        if s[j]==s[index]:
            times[j] = 0

print(result)



