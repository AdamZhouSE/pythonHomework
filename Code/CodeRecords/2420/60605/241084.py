# 将整数转换为两个无零整数的和
# 题目描述
# 「无零整数」是十进制表示中
# 不含任何
# 0
# 的正整数。
#
# 给你一个整数
# n，请你返回一个
# 由两个整数组成的列表[A, B]，满足：
#
# A
# 和
# B
# 都是无零整数
# A + B = n
# 题目数据保证至少有一个有效的解决方案。
#
# 如果存在多个有效解决方案，你可以返回其中任意一个。

def containsZero(n):
    return "0" in str(n)

if __name__ == '__main__':
    n = int(input())
    numL = 1
    numR = 0
    for numL in range(1, min(n, n//2+2)):
        if containsZero(numL):
            continue
        numR = n - numL
        if not containsZero(numR):
            break
    li = [numL, numR]
    print(li)