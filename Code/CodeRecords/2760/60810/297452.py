'''
给定房屋的街道（一排房屋），每个房屋内都存放有一定数量的钱；现在有一个小偷打算偷这笔钱，
但是他有一个限制/规定，他不能偷/抢两个相邻的房屋。找到他可以抢的最大钱。
'''


def getMaxMoney(n, money):
    res = 0
    half_n = n // 2
    res = (n - half_n) * money
    print(res)
    
    
t = int(input())
for i in range(0, t):
    inp = input().split(' ')
    n = int(inp[0])
    money = int(inp[1])
    getMaxMoney(n, money)