"""
给定一个N个整数的数组arr []
任务是查找数组中缺失的最小正数
注意：使用不变的额外空间，可以在O（n）时间内获得期望的解
"""

n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    arr=[int(m) for m in string_list[i+1].split(" ")]

    m=0
    while  m<len(arr):
        if arr[m]<0:
            del arr[m]
        else:
            m+=1

    while len(arr)>0:
        m = min(arr)
        del arr[arr.index(min(arr))]
        if len(arr)>0 and min(arr)!=m+1:
            break

    print(m+1)

    i+=2