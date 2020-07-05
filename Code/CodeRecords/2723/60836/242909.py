"""
给定一个非负整数num，请重复加所有数字，直到结果只有一位
如，给定98，则9+8：17，1+7：8
输出8
"""

n = int(input())
string_list = []

for i in range(n):
    string_list.append(str(input()))

for i in range(n):
    N = list(string_list[i])

    if len(N)==1:
        print(int(str(N[0])))
    else:
        while len(N)!=1:
            number=0
            for m in N:
                number=number+int(m)
            N=str(number)
        print(int(N))
