def YangHui (num = 10):
    LL = [[1]]
    for i in range(1,num):
        LL.append([(0 if j== 0 else LL[i-1][j-1])+ (0 if j ==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])
    return LL
n=int(input())
l=(YangHui(2*n-1))
print(l[2*n-2][n-1])
