"""
实现pow（A，B）％C。
给定A，B和C，找到（A^B）％C
"""


n = int(input())
string_list = []

for i in range(n):
    string_list.append(str(input()))

for i in range(n):
    int_list=string_list[i].split(" ")
    A=int(int_list[0])
    B=int(int_list[1])
    C=int(int_list[2])
    
    result=(A**B)%C
    
    print(result)