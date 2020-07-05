# 题目描述
# 你被锁在一个门上有数字键盘的房间里，
# 这个数字键盘有 10 个键，对应 0~9，同时你得到了一串数字序列，正确的密码是这个序列的最长而不一定连续的子序列。
# 你在键盘上发现了一些指纹，通过指纹得到按过的按键和数字序列，你能逃出这个房间吗？
#
# 输入描述
# 第一行包含两个整数 n 和 m  (1≤n,m≤10) 分别表示数字序列的长度和按过的按键的长度
# 第二行为这个数字序列
# 第三行为按过的按键
# 输出描述
# 输出这串数字密码，两两间用空格隔开
x = input().strip().split()
n = int(x[0])
m = int(x[1])

li = input().strip().split()
used = input().strip().split()
pwd = []
for i in li:
    if i in used: pwd.append(i)

for i in range(len(pwd)):
    print(pwd[i], end="")
    if i != len(pwd)-1: print(end=" ")
print()