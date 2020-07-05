"""
题目描述
给定结点数为n,边数为m的带权无向连通图G,所有结点编号为1,2,...,n。 求G的最小生成树的边权和。

输入描述
第一行两个正整数n, m。
之后的m行,每行三个正整数u_i(符号"_"表示下标),v_i,w_i(1≤u_i,v_i≤n, 0≤w_i≤10^9), 描述一条连接结点u_i和v_i,边权为w_i的边。
其中 1≤n≤2x10^5，0≤m≤5x10^5。
输出描述
一个整数表示G的最小生成树的边权和。
测试样例
样例1:输入-输出-解释
7 12
1 2 9
1 5 2
1 6 3
2 3 5
2 6 7
3 4 6
3 7 3
4 5 6
4 7 2
5 6 3
5 7 6
6 7 1

16
"""
def findParent(i,disjset:list):
    while disjset[i] != -1:
        i = disjset[i]
    return i

def union(i,j,disjset:list):
    disjset[findParent(i,disjset)] = j

def minimalSpanningTree(nodes,edges):
    edges = sorted(edges,key=lambda e:e[2])
    disjset = []
    totalWeight = 0
    count = 0
    for i in range(nodes):
        disjset.append(-1)
    for i in range(len(edges)):
        if findParent(edges[i][0]-1,disjset) != findParent(edges[i][1]-1,disjset):
            union(edges[i][0]-1,edges[i][1]-1,disjset)
            totalWeight += edges[i][2]
            count += 1
        #边数等于节点数-1
        if count == nodes-1:
            break
    print(totalWeight,end="")

if __name__ == "__main__":
    n,m = map(int,input().split(" "))
    edge = []
    for i in range(m):
        newedge = list(map(int,input().split(" ")))
        edge.append(newedge)
    minimalSpanningTree(n,edge)