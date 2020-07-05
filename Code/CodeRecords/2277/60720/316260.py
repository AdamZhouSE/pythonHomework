K=int(input())
N=int(input())
dpTable = [[0] * (K+1) for _ in range(2)]
m = 0
while(dpTable[1][-1] < N):
    m += 1
    # 把第二列交换到第一列
    dpTable[0] = dpTable[1][:]
    for k in range(1,K + 1):
        dpTable[1][k] = dpTable[0][k-1] + dpTable[0][k] +1
print(m)
