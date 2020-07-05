"""
2.22
Nim游戏
要想赢，就要把4块石头留给对手
即如果先手时有4n块石头，就会输
"""
num = int(input())
if num % 4 == 0:
    print("False")
else:
    print("True")
