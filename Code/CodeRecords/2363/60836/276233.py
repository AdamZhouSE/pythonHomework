"""
每个非负整数 N 都有其二进制表示。例如， 5 可以被表示为二进制 "101"，11 可以用二进制 "1011" 表示，依此类推
注意，除 N = 0 外，任何二进制表示中都不含前导零
二进制的反码表示是将每个 1 改为 0 且每个 0 变为 1。例如，二进制数 "101" 的二进制反码为 "010"
给定十进制数 N，返回其二进制表示的反码所对应的十进制整数
"""

N=int(input())

binary_list=[]
while N > 0:
    if N % 2 == 1:
        binary_list.append(1)
        N = (N - 1) // 2
    else:
        binary_list.append(0)
        N = N // 2
binary_list.reverse()

for i in range(len(binary_list)):
    if binary_list[i]==1:
        binary_list[i]=0
    else:
        binary_list[i]=1

result=0
for m in range(len(binary_list)):
    result = result + (2 ** (len(binary_list) - m - 1)) * binary_list[m]

print(result)