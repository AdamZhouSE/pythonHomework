class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        res = [[r0, c0]]
        four_corner = [[r0, c0 + 1], [r0 + 1, c0], [r0, c0 - 1], [r0 - 1, c0]]  # 记录四个方向每次开始的地方
        remaining_num = R * C - 1                # 剩余坐标数
        getNum = 2                               # 在一个方向上该次循环最多能取的坐标

        def change_corner():                     # 一个圆圈循环后，开始的点需要改变
            four_corner[0][0] -= 1
            four_corner[0][1] += 1
            four_corner[1][0] += 1
            four_corner[1][1] += 1
            four_corner[2][0] += 1
            four_corner[2][1] -= 1
            four_corner[3][0] -= 1
            four_corner[3][1] -= 1

        while remaining_num > 0:                  #超越边界的坐标将不计算（在许多max、min比较中去除）
            if 0 <= four_corner[0][1] < C:        #南方向
                for i in range(max(0, four_corner[0][0]), min(four_corner[0][0] + getNum, R)):
                    res.append([i, four_corner[0][1]])
                    remaining_num -= 1
            if 0 <= four_corner[1][0] < R:        #西方向
                for i in range(min(C - 1, four_corner[1][1]), max(-1, four_corner[1][1] - getNum), -1):
                    res.append([four_corner[1][0], i])
                    remaining_num -= 1
            if 0 <= four_corner[2][1] < C:        #北方向
                for i in range(min(R - 1, four_corner[2][0]), max(four_corner[2][0] - getNum, -1), -1):
                    res.append([i, four_corner[2][1]])
                    remaining_num -= 1
            if 0 <= four_corner[3][0] < R:        #东方向
                for i in range(max(0, four_corner[3][1]), min(four_corner[3][1] + getNum, C)):
                    res.append([four_corner[3][0], i])
                    remaining_num -= 1
            change_corner()                       #一个轮换改变四个方向开始的点
            getNum += 2                           #每个方向所能取的坐标数加2
        return res
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = Solution()
print(s.spiralMatrixIII(a,b,c,d))