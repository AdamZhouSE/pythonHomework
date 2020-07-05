"""
给定N个非负整数，其中每个代表坐标上的一个点（i，ai
绘制N条垂直线，使第i条线的两个端点位于（i，ai）和（i，0）
找到两条线，它们与x轴一起形成一个容器，以便该容器包含最多的水
"""

def next_max(arr):
    del arr[arr.index(max(arr))]
    return max(arr)



n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    N=string_list[i]
    arr=list(string_list[i+1])

    k=0
    while k<len(arr):
        if arr[k]==' ':
            del arr[k]
        k=k+1
    arr=[int(k) for k in arr]

    Max=0

    for m in range(len(arr)):
        k=m+1
        while k<len(arr):
            num=min(arr[m],arr[k])*(k-m)
            if Max<num:
                Max=num
            k=k+1

    print(Max)

    i=i+2