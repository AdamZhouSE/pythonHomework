"""
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值
如果数组元素个数小于 2，则返回 0
"""

arr=eval(input())

arr.sort()

i=0
max_sub=0
while i<len(arr)-1:
    if arr[i+1]-arr[i]>max_sub:
        max_sub=arr[i+1]-arr[i]
    i+=1

print(max_sub)