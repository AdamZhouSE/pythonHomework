"""
题目描述
    给定一个含有 n 个正数的数组 x。
    从点 (0,0) 开始，先向北移动 x[0] 米，然后向西移动 x[1] 米，向南移动 x[2] 米，向东移动 x[3] 米，持续移动。
    也就是说，每次移动后你的方位会发生逆时针变化。
    编写一个 O(1) 空间复杂度的一趟扫描算法，判断你所经过的路径是否相交。
"""


def isSelfCrossing(x):
    for i in range(3, len(x)):
        if x[i] >= x[i - 2] and x[i - 3] >= x[i - 1]:
            return True
        if i >= 4 and x[i - 1] == x[i - 3] and x[i] >= x[i - 2] - x[i - 4]:
            return True;
        if i >= 5 and x[i - 2] >= x[i - 4] and x[i - 3] >= x[i - 1] >= x[i - 3] - x[i - 5] and x[i] >= x[i - 2] - x[
            i - 4]:
            return True
    return False


print(isSelfCrossing(input().split(",")))
