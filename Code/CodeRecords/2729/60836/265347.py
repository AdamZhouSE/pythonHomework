"""
给定一个只包含整数的有序数组，每个元素都会出现两次
唯有一个数只会出现一次，找出这个数
您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行
"""

a=input()
arr=eval(a)

while len(arr)>0:
    a=arr[0]
    del arr[0]
    if a in arr:
        del arr[arr.index(a)]
    else:
        print(a)
        break
