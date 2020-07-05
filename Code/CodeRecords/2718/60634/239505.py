def combine(d1, d2, disjoint):  # 合并并查集
    disjoint[d1].extend(disjoint[d2])
    disjoint.remove(disjoint[d2])


def search(index, disjoint):  # 搜索下标所在并查集号
    result = -1
    i = 0
    while i < len(disjoint):
        for k in disjoint[i]:
            if k == index:
                return i
        i += 1
    return result


def insert(pairs, disjoint):  # 插入并查集
    setNum0 = search(pairs[0], disjoint)
    setNum1 = search(pairs[1], disjoint)
    if (setNum0 == -1) and (setNum1 == -1):
        disjoint.append([pairs[0], pairs[1]])
    elif setNum0 == -1:
        disjoint[setNum1].append(pairs[0])
    elif setNum1 == -1:
        disjoint[setNum0].append(pairs[1])
    elif setNum0 != setNum1:
        combine(setNum0, setNum1, disjoint)
    # else setNum0 == setNum1:
    # nothing to do
    return


def sort(str, set):  # 对特定下标排序
    setSort(set)
    theStr = [0 for x in range(len(set))]
    i = 0
    while i < len(set):
        theStr[i] = str[set[i]]
        i += 1
    setSort(theStr)
    i = 0
    j = 0
    while i < len(str):
        if (j < len(set))and(i == set[j]):
            str[i] = theStr[j]
            j += 1
        i += 1



def setSort(set):
    i = 0
    while i < len(set):
        j = len(set)-1
        while j > i:
            if set[j] < set[j-1]:
                temp = set[j]
                set[j] = set[j -1]
                set[j-1] = temp
            j -= 1
        i += 1


# main-----
source = input()
pairSet = eval(input())
disjoint = []  # 并查集
# 字符串转数组
str = []
for ch in source:
    str.append(ch)
# 构建并查集
for pairs in pairSet:
    insert(pairs, disjoint)
# 对数组排序
for set in disjoint:
    sort(str,set)
# 数组转字符串
result = ""
for ch in str:
    result += ch
# 输出
print(result)

