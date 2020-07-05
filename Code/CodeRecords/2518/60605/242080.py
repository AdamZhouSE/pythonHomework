# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
# 现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
#
# 所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
#
# 说明:
#
# 给出的房屋和供暖器的数目是非负数且不会超过 25000。
# 给出的房屋和供暖器的位置均是非负数且不会超过10^9。
# 只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
# 所有供暖器都遵循你的半径标准，加热的半径也一样。

homes = "["+input()+"]"
stations = "["+input()+"]"
homes = list(eval(homes))
stations = list(eval(stations))
maxLen = 0
for i in homes:
    minLen = 999999999999999
    for j in stations:
        minLen = min(minLen, abs(j-i))
    maxLen = max(maxLen, minLen)
print(maxLen)
