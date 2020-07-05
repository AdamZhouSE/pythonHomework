"""
2.19
系统管理员
"""
amount = int(input())
num1 = 0
num2 = 0
for i in range(0, amount):
    data = input().split(" ")
    # 分别计算ping 1与ping 2，接收到的包超过一半就是：所有接收-所有丢失>=0
    if data[0] == "1":
        num1 += int(data[1]) - int(data[2])
    else:
        num2 += int(data[1]) - int(data[2])
if num1 >= 0:
    print("LIVE")
else:
    print("DEAD")
if num2 >= 0:
    print("LIVE")
else:
    print("DEAD")
