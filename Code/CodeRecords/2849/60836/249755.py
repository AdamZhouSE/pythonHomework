"""
给定一个由 n 个正整数组成的数组
请在数组中找到这样一个数，所有数组元素都可以被它整除
"""

n=int(input())
arr=[int(k) for k in str(input()).split(" ")]
num=-1

for i in arr:
    result = True
    for m in arr:
        if m%i!=0:
            result=False
            break
    if result:
        num=i

print(num)