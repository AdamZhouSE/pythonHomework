def cheapest_flight(flights,n,src,dst,k):
    INT_MAX=1000000
    # matrix 表示从src到达第i行最多经过k步的最小花费
    matrix=[[INT_MAX for _ in range(k+2)]for _ in range(n)]
    for x in range(k+2):
        matrix[src][x]=0  # src到src不管经过多少站的花费都是0

    for x in range(1,k+2):
        for f in flights:
            if matrix[f[0]][x-1]!=INT_MAX:
                matrix[f[1]][x]=min(matrix[f[1]][x],matrix[f[0]][x-1]+f[2])

    if matrix[dst][k+1] == INT_MAX:
        return -1
    else:
        return matrix[dst][k+1]

n=int(input())
flights=eval(input())
src=int(input())
dst=int(input())
k=int(input())
res=cheapest_flight(flights,n,src,dst,k)

print(res)