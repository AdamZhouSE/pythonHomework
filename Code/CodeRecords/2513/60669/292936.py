n=eval(input())
matrix=[[None]*n for i in range(n)]
for i in range(n):
    matrix[i]=list(map(int,input().split(",")))
k=eval(input())
left=matrix[0][0]
right=matrix[n-1][n-1]
import math

while left<right:
    mid=math.floor((left+right)/2)   # 这是个数 不是索引   但mid不一定在matrix里啊
    temp=0
    for i in range(n):
        for j in range(n):
            num=matrix[i][j]
            if num<=mid:
                temp+=1
            elif j==0:
                break     # 若某行的第一个数字都比要mid大 那么这行及下面的行的数字都会比mid大了
    if temp<k:
        left=mid+1
    elif temp>=k:
        right=mid

print(right)