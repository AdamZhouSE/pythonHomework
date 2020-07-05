"""
你被锁在一个门上有数字键盘的房间里，这个数字键盘有 10 个键，对应 0~9
同时你得到了一串数字序列，正确的密码是这个序列的最长而不一定连续的子序列
你在键盘上发现了一些指纹，通过指纹得到按过的按键和数字序列
你能逃出这个房间吗？
"""

NM=input()
arr=str(input()).split(" ")
pp=str(input()).split(" ")    #a part of the password
password=[]

for i in arr:
    for m in pp:
        if m==i:
            password.append(m)

print(" ".join(password))