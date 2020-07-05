# 题目描述
# 给定一个非负整数num，请重复加所有数字，直到结果只有一位。
#
# 输入描述
# 第一行包含“ T”，表示测试用例的数量。然后是测试用例的描述。接下来的T行包含一个表示N值的整数N。
#
# 输出描述
# 输出所有数字的总和，直到结果只有一位。

def plusUntil(liOfNum) :
    sum = 0
    for i in liOfNum:
        sum += int(i)
    if sum < 10:
        return sum
    else:
        return plusUntil(list(str(sum)))

t = int(input())
li = []
for i in range(t):
    li.append(input())

for i in range(t):
    print(plusUntil(list(str(li[i]))))