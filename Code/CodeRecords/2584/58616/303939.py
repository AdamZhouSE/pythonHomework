# LeetCode 292
# 如果堆中石头的数量n不能被4整除，那么你总是可以胜利
def canWinNim(n):
    return n % 4 != 0


num = eval(input())
print(canWinNim(num))