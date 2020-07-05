#27
#本题大概是个动态规划的问题，要实时更新最高分的人，之前没想明白就面向用例了，再写一次
n = int(input())
dic = {}
maxName = ""
maxValue = 0
for i in range(0,n):
    ori = input().split(" ")
    if ori[0] not in dic:
        dic[ori[0]] = int(ori[1])
    else:
        dic[ori[0]] += int(ori[1])
    if dic[ori[0]] > maxValue:
        maxName = ori[0]
        maxValue = dic[ori[0]]
print(maxName)