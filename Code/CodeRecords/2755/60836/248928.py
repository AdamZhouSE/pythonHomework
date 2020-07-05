"""
给定两个由多项式的两个数组表示的多项式，以多项式相乘后形成的数组形式打印多项式
第一多项式： 1 + 0x ^ 1 + 3x ^ 2 + 2x ^ 3
第二多项式： 2 + 0x ^ 1 + 4x ^ 2
结果多项式： 2 + 0x ^ 1 + 10x ^ 2 + 4x ^ 3 + 12x ^ 4 + 8x ^ 5
"""


n=int(input())
string_list = []

for i in range(n*3):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    N=string_list[i]
    arr1=[int(m) for m in string_list[i+1].split(" ")]
    arr2=[int(m) for m in string_list[i+2].split(" ")]

    result=[int(0) for m in range(len(arr1)+len(arr2)-1)]

    for m in range(len(arr2)):
        for k in range(len(arr1)):
            result[m+k]=result[m+k]+arr2[m]*arr1[k]

    result=[str(m) for m in result]
    print(" ".join(result))

    i=i+3