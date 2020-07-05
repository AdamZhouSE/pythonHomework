"""
给定两个表示两个整数值的二进制字符串，请找到两个字符串的乘积
例如，如果第一位字符串为“ 1100”，第二位字符串为“ 1010”
则输出应为120
"""

n=int(input())
string_list = []

for i in range(n):
    string_list.append(str(input()))

i=0
for i in range(n):
    NM=string_list[i].split(" ")
    a=NM[0]
    b=NM[1]
    resulta=0
    resultb=0

    for m in range(len(a)):
        resulta=resulta+(2**(int(len(a))-m-1))*int(a[m])
    for m in range(len(b)):
        resultb=resultb+(2**(int(len(b))-m-1))*int(b[m])

    result=resulta*resultb

    print(result)
