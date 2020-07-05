# 题目描述
# 给定字符串“ s”。任务是查找最小窗口长度，该窗口长度至少包含一次给定字符串的所有字符。
#
# 例如。 A =“ aabcbcdbca”，那么结果将是4，因为最小的窗口将是“ dbca”。
#
# 输入描述
# 输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。每个测试用例都包含一个字符串S。
#
# 输出描述
# 对于换行中的每个测试用例，请打印最小的字符串长度。

t = int(input())
li = []
for i in range(t):
    li.append(list(input().strip()))
# print(li)
for s in li:
    num = len(set(s))
    # print("num", num)
    # print(len(s)+1)
    isOK = False
    for i in range(num, len(s)+1):
        # i is chosen length
        for begin in range(0, len(s)-i+1):
            # print(s[begin:begin+i])
            if len(set(list(s[begin: begin+i]))) == num:
                print(i)
                isOK = True
                break
        if isOK: break