"""
桌子上有 n 个石头排成一排，可能为红色，绿色和蓝色
请你移除最少数量的石头使得相邻石头的颜色均不同。
"""

n=int(input())
arr=list(str(input()))

m=1
number=0
while m<len(arr):
    if arr[m]==arr[m-1]:
        number=number+1
    m=m+1
    
print(number)