n=int(input())
edges=eval(input())
src=int(input())
dst=int(input())
k=int(input())
prices=[[1000000 for i in range(k+1)] for j in range(n)]
#prices[i][k]表示从src到i经过最多k个中转站的最低费用
for j in range(k+1):
    prices[src][j]=0
for edge in edges:
    if(edge[0]==src):
        for j in range(k+1):
            prices[edge[1]][j]=edge[2]
for edge in edges:
    for i in range(k):
        if(prices[edge[0]][i]!=1000000):
            prices[edge[1]][i+1]=min(prices[edge[1]][i+1],prices[edge[0]][i]+edge[2])
print(prices[dst][k])