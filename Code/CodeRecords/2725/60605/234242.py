# 题目描述
# 很长一段时间以来，汤姆和杰里一直在争夺一块奶酪。
# 所以最后你来营救，并决定战斗的结果将由一个数学游戏决定，
# 其中你将写一个数字N。
# 汤姆和杰里将交替玩游戏，他们每个人都会减去数字n [n <N]，使得N％n = 0。
# 游戏被逐个重复进行，直到不能再进一步移动的那个游戏为止。
# 游戏以汤姆开始，众所周知，他们两个都将以最佳方式进行动作，您将确定谁赢得了比赛。
#
# 输入描述
# 输入的第一行包含一个整数T，表示测试用例的数量，然后是T测试用例。每个测试用例的第一行由N个数字组成。
#
# 输出描述
# Print 1 if Tom wins and Print 0 if Jerry wins in a separate line.
import math

def isprime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def maxDiv(n):
    tmp = n // 2
    if n == tmp:
        tmp = n - 1
    while True:
        if n % tmp == 0:
            break
        else:
            tmp -= 1
    print("maxDiv", tmp)
    return tmp


t = int(input())
li = []
for i in range(t):
    li.append(int(input()))

for i in li:
    if i % 2 == 0:
        print("1")
    else:
        print("0")
            