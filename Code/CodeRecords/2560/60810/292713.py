'''
给定项目数组，第i个索引元素表示项目ID，给定数字m，则任务是删除m个元素，以使剩余的唯一ID最少。打印不同ID的数量。
'''


def isIn(temp, lis):
    for i in range(0, len(lis)):
        if temp == lis[i]:
            return True
    return False


def delID(n, id, m):
    diff = []
    for i in range(0, len(id)):
        if isIn(id[i], diff):
            continue
        else:
            diff.append(id[i])
    allDiff = len(diff)
    nums = []
    for i in range(0, allDiff):
        nums.append(0)
    for i in range(0, allDiff):
        for c in id:
            if c == diff[i]:
                nums[i] += 1
    for tmp in nums:
        if tmp <= m:
            allDiff -= 1
            m -= tmp
        if tmp > m:
            break
    if allDiff == 2:
        return 1
    return allDiff


t = int(input())
for i in range(0, t):
    n = int(input())
    id = input().split(' ')
    m = int(input())
    res = delID(n, id, m)
    print(res)