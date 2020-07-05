"""
给你一个由 n 个整数组成的数组 a
你的任务是找到数组中所有元素的公约数的数量
例如，如果数组 a 为 [2,4,6,2,10]
则 1 和 2 为这个数组的公约数（因此答案为2）
"""

n=int(input())
arr=[int(m) for m in str(input()).split(" ")]

m=1
num=0
while m<=min(arr):
    isdivisor=True
    for i in arr:
        if i%m!=0:
            isdivisor=False
    if isdivisor:
        num+=1
    m+=1

print(num)