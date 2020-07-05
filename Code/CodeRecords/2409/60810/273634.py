'''
数轴上放置了一些筹码，每个筹码的位置存在数组 chips 当中。
你可以对 任何筹码 执行下面两种操作之一（不限操作次数，0 次也可以）：
将第 i 个筹码向左或者右移动 2 个单位，代价为 0。
将第 i 个筹码向左或者右移动 1 个单位，代价为 1。
最开始的时候，同一位置上也可能放着两个或者更多的筹码。
返回将所有筹码移动到同一位置（任意位置）上所需要的最小代价。
'''

inp = input()
chips = inp[0:].split(",")
chips = list(map(int, chips))

odd = 0
eve = 0
for i in range(0,len(chips)):
    if (chips[i] % 2 == 0):
        eve += 1
    else:
        odd += 1
if eve >= odd:
    print(odd)
else:
    print(eve)
