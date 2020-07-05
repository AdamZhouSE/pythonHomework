"""
给定 n×n 棋盘。 板上的每个单元格都有字符 x 或字符 o
请确认板上的每个单元格上下左右合计都有偶数个的 o（0 也是偶数）
"""

n=int(input())
arr=[]

for i in range(n):
    arr.append(str(input()))

result=True
for i in range(len(arr)):
    for m in range(len(arr[i])):
        num_of_o=0
        up=i-1
        down=i+1
        left=m-1
        right=m+1
        if up>=0 and arr[up][m]=='o':
            num_of_o+=1
        if down<n and arr[down][m]=='o':
            num_of_o+=1
        if left>=0 and arr[i][left]=='o':
            num_of_o+=1
        if right<n and arr[i][right]=='o':
            num_of_o+=1
        if num_of_o%2==1:
            result=False
            break

if result:
    print("YES")
else:
    print("NO")