import math
"""
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)
"""

arr=eval(input())

m=math.floor(len(arr)/3)
result=[]

for i in arr:
    if arr.count(i)>m and i not in result:
        result.append(i)

print(result)
