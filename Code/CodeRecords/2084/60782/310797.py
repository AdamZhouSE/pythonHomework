"""
题目描述
给一个n(1<=n<=2500)个点m(1<=m<=6200)条边的无向图，求s到t的最短路。

输入描述
第一行四个由空格隔开的整数n、m、s、t。
之后的m行，每行三个正整数s_i（符号“_”表示下标）、t_i、w_i(1<=W_i<=10^9)，表示一条从s_i到t_i长度为w_i的边。
输出描述
一个整数表示从s到t的最短路长度。数据保证至少存在一条道路。
测试样例
样例1:输入-输出-解释
7 11 5 4
2 4 2
1 4 3
7 2 2
3 4 3
5 7 5
7 3 3
6 1 1
6 3 4
2 4 3
5 6 3
7 2 1

7
"""
def addEdge(newedge:list,edges:list):
    newWeight = newedge[2]
    index = 0
    while index < len(edges):
        if edges[index][2] > index:
            break
        index += 1
    edges.insert(index,newedge)

def minWay(src:int,dest:int,edges:list):
    weights = {}
    weights[src] = 0
    while not dest in weights:
        #选择最短的边
        minWeight = 2**31-1
        i = 0
        newVertice = -1
        while i < len(edges):
            headAdded = edges[i][0] in weights
            tailAdded = edges[i][1] in weights
            #如果两个端点都可达了就删掉
            if headAdded and tailAdded:
                del edges[i]
                i -= 1
            elif headAdded and not tailAdded:
                if edges[i][2] + weights[edges[i][0]] < minWeight:
                    minWeight = edges[i][2] + weights[edges[i][0]]
                    newVertice = edges[i][1]
            elif not headAdded and tailAdded:
                if edges[i][2] + weights[edges[i][1]] < minWeight:
                    minWeight = edges[i][2] + weights[edges[i][1]]
                    newVertice = edges[i][0]
            i += 1
        if newVertice != -1:
            weights[newVertice] = minWeight
    print(weights[dest])

if __name__ == "__main__":
    n,m,src,dest = map(int,input().split())
    edges = []
    for i in range(m):
        edge = []
        s,t,w = map(int,input().split())
        edge.append(s)
        edge.append(t)
        edge.append(w)
        edges.append(edge)
    minWay(src,dest,edges)