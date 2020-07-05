"""
在N * N棋盘中找到正方形总数
"""

n = int(input())
string_list = []

for i in range(n):
    string_list.append(int(input()))

for i in range(n):
    N=int(string_list[i])

    number=0

    m=1
    while m<=N:
        number=number+m*m
        m=m+1

    print(number)