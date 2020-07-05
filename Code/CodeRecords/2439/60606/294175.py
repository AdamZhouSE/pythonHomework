# (a xor b) xor (a xor c) = b xor c
#所有随意选取一个根节点就可以了，然后去看询问的开始和结束
import numpy as np

n = int(input())
#初始化图
mat_origin = [-1]*(n*n)
mat = np.array(mat_origin).reshape(n,n)
result = [-1]*n
for i in range(n):
    mat[i][i] = 0
for i in range(n-1):
    line = input().split(" ")
    line = [int(x) for x in line]
    x = line[0]-1
    y = line[1] -1
    value = line[2]
    mat[x][y] = value
dis = [0]*n
def dfs(start,pre):
    for i in range(0,n):
        #边存在就把目的点放入集合，并且更新距离，并dfs
        if mat[start][i] != -1 and start!=i and i!=pre:
            dis[i] = dis[start]^mat[start][i]
            dfs(i,start)
        elif mat[i][start] != -1 and start!=i and i!=pre:
            dis[i] = dis[start]^mat[i][start]
            dfs(i,start)
dfs(0,0)
#根据询问数据输出
query_num = int(input())
for i in range(query_num):
    temp = input().split(" ")
    temp = [int(x) for x in temp]
    start = temp[0]-1
    end = temp[1]-1
    if start == end:
        print(0)
    else:
        print(dis[start]^dis[end])



