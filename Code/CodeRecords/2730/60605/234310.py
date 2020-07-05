# 题目描述
# 给定一个整数数组，任务是查找是否有可能使用这些数字的所有数字来构造一个整数，使得该整数可以被3整除。如果可能，则打印“ 1”，否则打印“ 0” 。
#
# 输入描述
# 第一行由整数T组成，即测试用例的数量。每个测试用例的第一行包含一个整数n。下一行由n个间隔的整数组成。
#
# 输出描述
# 如果可以使用数组元素形成一个可被3整除的数字，则打印“ 1”，否则打印“ 0”。

t = int(input())
li = []
for i in range(t):
    input()
    li.append(input())

for i in range(t):
    cnt = 0
    for j in li[i]:
        if j.isdigit():
            cnt += int(j)
    if cnt % 3 == 0:
        print("1")
    else:
        print("0")


