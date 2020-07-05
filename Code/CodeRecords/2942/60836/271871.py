"""
设有n个正整数(n≤20)，将它们联接成一排，组成一个最大的多位整数
例如：n=3时，3个整数13,312,343联接成的最大整数为：34331213
又如：n=4时，4个整数7,13,4,246联接成的最大整数为：7424613
"""

n=int(input())
arr=str(input()).split(" ")

arr.sort()
arr.reverse()
print(int("".join(arr)),end='')

