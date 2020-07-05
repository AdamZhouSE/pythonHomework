def judge(point, val):
    index = nodes.index(point)
    if value[index] == val:
        return True
    elif leftS[index] == 0 and rightS[index] == 0:
        return False
    elif leftS[index] != 0 and rightS[index] == 0:
        return judge(leftS[index], val-value[index])
    elif leftS[index] == 0 and rightS[index] != 0:
        return judge(rightS[index], val - value[index])
    else:
        return judge(leftS[index], val-value[index]) or judge(rightS[index], val - value[index])


def find_short_path(point, val):
    index = nodes.index(point)
    if value[index] == val:
        if leftS[index] != 0 and judge(leftS[index], 0):
            return 1 + find_short_path(leftS[index], 0)
        elif rightS[index] != 0 and judge(rightS[index], 0):
            return 1 + find_short_path(rightS[index], 0)
        else:
            return 1
    elif leftS[index] != 0 and rightS[index] == 0:
        return 1 + find_short_path(leftS[index], val - value[index])
    elif leftS[index] == 0 and rightS[index] != 0:
        return 1 + find_short_path(rightS[index], val - value[index])
    else:
        if judge(leftS[index], val - value[index]) and judge(rightS[index], val - value[index]):
            return 1 + min(find_short_path(leftS[index], val - value[index]), find_short_path(rightS[index], val - value[index]))
        elif (not judge(leftS[index], val - value[index])) and judge(rightS[index], val - value[index]):
            return 1 + find_short_path(rightS[index], val - value[index])
        else:
            return 1 + find_short_path(leftS[index], val - value[index])


inp = input().strip().split(" ")
t = int(inp[0])
root = int(inp[1])
nodes = []
leftS = []
rightS = []
value = []
for i in range(t):
    li = input().strip().split(" ")
    nodes.append(int(li[0]))
    leftS.append(int(li[1]))
    rightS.append(int(li[2]))
    value.append(int(li[3]))
target = int(input())
shortPath = 0
for k in nodes:
    if judge(k, target):
        leng = find_short_path(k, target)
        if leng > shortPath:
            shortPath = leng
print(shortPath)
