"""
你现在拿到一个由 24 个 0 和 1 个 1 组成的 5*5 的矩阵
现在你需要把这个 1 移动到矩阵的中心点，使得这个矩阵变得 “优雅”
只能上下左右一格一格移动，请你输出最小移动数
"""

arr=[]
for i in range(5):
    arr.append(str(input()).split(" "))

x=0
y=0
for i in range(5):
    for m in range(5):
        if arr[i][m]=='1':
            x=i
            y=m
            break

step=abs(x-2)+abs(y-2)
print(step)