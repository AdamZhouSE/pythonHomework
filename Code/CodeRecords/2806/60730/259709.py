num = int(input())
n = {}              #按行输入的二维数组用字典实现
for i in range(num):
    n[i] = list(map(int, input().split()))
tmp = 0
minnum = n[0][1]
for j in range(num-1):
    if n[j][1] <= n[j+1][1]:
        tmp = tmp + n[j][0]*minnum
    else:
        tmp = tmp + n[j][0] * n[j][1]
        minnum = n[j + 1][1]
tmp = tmp + n[num-1][0]*minnum
print(tmp)
