"""
一个 n × n 的矩阵 a 是这样定义的:
第一行和第一列包含： a[i][1] = a[1][i]=1 对于所有的 i = 1, 2, ..., n.
表中剩余的每个数字等于它上面的数字和它的左边的数字的总和。换句话说，其余元素由公式 a[i][j] = a[i-1][j] + a[i][j-1] 定义
这些条件定义表中的所有值。
给你一个数 n，你需要求出给定的 n × n 的矩阵中最大的数
"""

n=int(input())
arr=[]

for i in range(n):
    arr.append([1])

for i in range(n):
    arr[0].append(1)

m=1
while m<n:
    k=1
    while k<n:
        arr[m].append(arr[m-1][k]+arr[m][k-1])
        k+=1
    m+=1

print(arr[n-1][n-1])