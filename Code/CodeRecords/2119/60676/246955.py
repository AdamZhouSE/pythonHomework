# 给定一个含有 n 个正数的数组 x。
# 从点 (0,0) 开始，先向北移动 x[0] 米，然后向西移动 x[1] 米，向南移动 x[2] 米，向东移动 x[3] 米，持续移动。
# 也就是说，每次移动后你的方位会发生逆时针变化。
# 编写一个 O(1) 空间复杂度的一趟扫描算法，判断你所经过的路径是否相交。


def fun(arr):
    if arr[0] >= arr[2] and arr[1] <= arr[3]:
        return True
    return False


print(fun(eval(input())))