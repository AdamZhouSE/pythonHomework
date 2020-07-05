# LeetCode 991
# 逆向思维，令y -> x，贪心地做除法操作，再做加法操作即可
def opreationTimes(x, y):
    times = 0
    while (y > x):
        if (y % 2 == 0):
            y /= 2
            times += 1
        else:
            y += 1
            y /= 2
            times += 2
    while (y != x):
        times += 1
        y += 1
    return times


x = eval(input())
y = eval(input())
print(opreationTimes(x, y))