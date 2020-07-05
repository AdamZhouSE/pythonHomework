# 二维输入
listList = input().strip('[|]').split('],[')
listList = [[int(i) for i in j.split(',')] for j in listList]
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())
listList = [i for i in listList if i[2] >= veganFriendly and i[3] <= maxPrice and i[4] <= maxDistance]
listList.sort(key=lambda x: (-x[1], -x[0]))
print([i[0] for i in listList])