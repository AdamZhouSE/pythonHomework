"""
小凸和小方是好朋友，小方给小凸一个N * M（N≤M）的矩阵A，要求小凸从其中选出N个数
其中任意两个数字不能在同一行或同一列，现小凸想知道选出来的N个数中第K大的数字的最小值是多少
"""

NMK=[int(m) for m in str(input()).split(" ")]

N=NMK[0]
M=NMK[1]
K=NMK[2]

arr=[]
for i in range(N):
    arr.append([int(m) for m in (str(input()).strip()).split(" ")])

min_num=[]
index=[]
for i in range(N):
    inde = arr[i].index(min(arr[i]))
    index.append(inde)
    min_num.append(min(arr[i]))

min_num.sort()
print(min_num[K-1])