"""
在给定的直方图中找到最大的矩形区域，其中最大的矩形可以由许多连续的条形组成
为简单起见，假设所有条形都具有相同的宽度，并且宽度为1个单位
"""

n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    N=string_list[i]
    arr=[int(k) for k in string_list[i+1].split(" ")]
    Max=0

    for m in range(len(arr)):
        k=m+1
        while k<=len(arr):
            num=min(arr[m:k])*(k-m)
            if Max<num:
                Max=num
            k=k+1

    print(Max)

    i=i+2