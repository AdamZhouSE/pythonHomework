"""
给定房屋的街道（一排房屋），每个房屋内都存放有一定数量的钱
现在有一个小偷打算偷这笔钱，但是他有一个限制/规定，他不能偷/抢两个相邻的房屋
找到他可以抢的最大钱
"""

n = int(input())
string_list = []

for i in range(n):
    string_list.append(str(input()))

for i in range(n):
    str_list=string_list[i].split(" ")
    M=int(str_list[0])
    N=int(str_list[1])

    money=0

    if M%2==0:
        money=N*(M//2)
    else:
        money=N*((M+1)//2)

    print(money)