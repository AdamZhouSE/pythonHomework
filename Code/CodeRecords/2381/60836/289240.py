import math
"""
给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果
数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列
例如，arr = [1,1,0,1] 表示数字 (-2)^3 + (-2)^2 + (-2)^0 = -3
数组形式 的数字也同样不含前导零：以 arr 为例，这意味着要么 arr == [0]，要么 arr[0] == 1
返回相同表示形式的 arr1 和 arr2 相加的结果
两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组
"""

arr1=eval(input())
arr2=eval(input())

n1=0
n2=0
for i in range(len(arr1)):
    n1=n1+(-2)**(len(arr1)-1-i)*(arr1[i])
for i in range(len(arr2)):
    n2=n2+(-2)**(len(arr2)-1-i)*(arr2[i])

N=n1+n2
re=[]
while N!=1:
    if N%(-2)==(-1):
        re.append(1)
    else:
        re.append(0)
    N=math.ceil(N/(-2))

re.append(1)
re.reverse()
print(re)