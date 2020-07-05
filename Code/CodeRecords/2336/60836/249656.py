"""
给定一个数组A和一个整数K
找到大小为K的每个连续子数组的最大值
"""

n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    NM=string_list[i].split(" ")
    N=int(NM[1])
    arr=[int(m) for m in string_list[i+1].split(" ")]

    result=[]

    m=0
    while m<len(arr)-N+1:
        result.append(max(arr[m:m+N]))
        m=m+1

    print(" ".join([str(c) for c in result])+" ")

    i=i+2