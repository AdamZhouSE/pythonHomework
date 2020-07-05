# 题目描述
# 给定一次选举中候选人的姓名数组（由小写字母组成）。
# 数组中的候选人名称表示对候选人的投票。打印获得最高票数的候选人的姓名。如果有平局，则按字典顺序打印较小的名称。
#
# 输入描述
# 输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。每个测试用例包含两行： 票数N 候选人的姓名，以空格分隔。每个名字代表对该候选人投一票。
#
# 输出描述
# 对于每个测试用例，请打印出具有最高票数的候选人的姓名，并同时打印为该候选人投下的票。名称和投票之间用空格隔开。

# 2
# 13
# john johnny jackie johnny john jackie jamie jamie john johnny jamie johnny john
# 3
# andy blake clark

t = int(input())
liOfGroups = []
liOfCnt = []
for i in range(t):
    liOfCnt.append(int(input()))
    liOfGroups.append(input().split(" "))

for i in range(t):
    group = liOfGroups[i]
    cnt = liOfCnt[i]
    dictOfGroup = {}
    # print("key" in dictOfGroup.keys())
    for vote in group:
        if vote in dictOfGroup.keys():
            dictOfGroup[vote] = dictOfGroup[vote] + 1
        else:
            dictOfGroup[vote] = 1
    dictOfGroup = sorted(dictOfGroup.items(), key=lambda mapp:(-mapp[1], mapp[0]), reverse=False)
    print(dictOfGroup[0][0], dictOfGroup[0][1])
