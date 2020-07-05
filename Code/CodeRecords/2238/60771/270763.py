#20
ori = input().split(",")
dic = {}
minNum = 0
for item in ori:
    if item not in dic:
        dic[item] = 1
    else:
        dic[item] += 1
for item in dic:
    ordinary = int(item) + 1
    ordinary = max(ordinary,dic[item])
    minNum += ordinary
print(minNum)