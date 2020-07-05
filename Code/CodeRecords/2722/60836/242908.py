"""
给定一个整数N，您必须确定它是否是Anshuman的最爱
如果是，则打印“YES”，否则打印“NO”
如果数字是整数5的和或差，则它是Anshuman的最爱（5 + 5、5 + 5 + 5、5-5、5-5-5 + 5 + 5…..）
"""

n = int(input())
string_list = []

for i in range(n):
    string_list.append(int(input()))

for i in range(n):
    N = string_list[i]

    if N%5==0:
        print("YES")
    else:
        print("NO")