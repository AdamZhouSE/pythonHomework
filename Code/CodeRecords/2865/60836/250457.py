"""
肖恩要把一个 m GB 的大文件保存到一个U盘上
他有 n 个U盘，容量分别为 a1, a2, ..., an GB
假设这个大文件可以被分成任意份存储，请帮助肖恩计算最少需要的U盘数量
"""

n=int(input())
U=int(input())
U_list=[]

for i in range(n):
    U_list.append(int(input()))

number=0
while U>0:
    U=U-max(U_list)
    del U_list[U_list.index(max(U_list))]
    number=number+1

print(number)