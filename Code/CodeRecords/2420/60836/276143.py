"""
「无零整数」是十进制表示中 不含任何 0 的正整数
给你一个整数 n，请你返回一个 由两个整数组成的列表 [A, B]，满足：
A 和 B 都是无零整数
A + B = n
如果存在多个有效解决方案，你需要递增返回其中一个
"""

def has_zero(num):
    arr=list(str(num))
    for i in arr:
        if i=='0':
            return True
    return False


n=int(input())

A=1
B=n-1
while has_zero(A) or has_zero(B):
    A+=1
    B-=1

print([A,B])