"""
题目描述
    给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
    此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
"""
"""
输入描述
    一个未排序的数组
"""
"""
输出描述
    排好序的数组
"""
currInput = input()
sample = currInput[1:-1].split(',')
currOutcome = sample
outcome = []
for items in currOutcome:
    if items == '0':
        outcome = outcome + [0]
    elif items == '1':
        outcome = outcome + [1]
    elif items == '2':
        outcome = outcome + [2]
for index in range(len(sample)):
    if outcome[index] == 0:
        del outcome[index]
        outcome.insert(0, 0)
    elif outcome[index] == 2:
        del outcome[index]
        outcome.append(2)
print(outcome)
