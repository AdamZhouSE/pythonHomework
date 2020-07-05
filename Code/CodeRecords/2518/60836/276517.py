"""
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖
现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径
所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径
说明:
给出的房屋和供暖器的数目是非负数且不会超过 25000
给出的房屋和供暖器的位置均是非负数且不会超过10^9
只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖
所有供暖器都遵循你的半径标准，加热的半径也一样
"""

def get_r(room,heater):
    begin=0
    while begin<len(heater)-1:
        if room>=heater[begin] and room<=heater[begin+1]:
            return min(heater[begin+1]-room,room-heater[begin])
        begin+=1
    return min(abs(room-min(heater)),abs(max(heater)-room))


room=[int(m) for m in str(input()).split(",")]
heater=[int(m) for m in str(input()).split(",")]

max_r=0
for i in room:
    r=get_r(i,heater)
    if r>max_r:
        max_r=r

print(max_r)