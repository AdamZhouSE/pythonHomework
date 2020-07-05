"""
给定范围[m..n],您的任务是找到在给定范围内被a或b整除的整数数量
输入的第一行由表示测试用例数量的整数T组成
下一行由四个以空格分隔的整数m，n，a，b组成，其中m和n表示范围
"""

n = int(input())
string_list = []

for i in range(n):
    string_list.append(str(input()))

for i in range(n):
    str_list=string_list[i].split(" ")
    M=int(str_list[0])
    N=int(str_list[1])
    a=int(str_list[2])
    b=int(str_list[3])

    number=0

    while M<=N:
        if M%a==0 or M%b==0:
            number=number+1
        M=M+1

    print(number)