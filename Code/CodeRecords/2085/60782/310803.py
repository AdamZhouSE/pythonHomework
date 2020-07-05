"""
题目描述
给定包含n个结点，m条有向边的一个图。试求一棵以结点r为根的最小树形图,并输出最小树形图每条边的权值之和,如果没有以r为根的最小树形图，输出-1。

输入描述
第一行包含三个整数n,m,r,意义同题目所述。
接下来m行，每行包含三个整数u, v, w,表示图中存在一从u指向V的权值为w的有向边。
对于所有数据，1≤u,v≤n≤100,1≤m≤10^4,1≤w≤10^6。
输出描述
如果原图中存在以r为根的最小树形图,就输出最小树形图每条边的权值之和，否则输出-1。
测试样例
样例1:输入-输出-解释
4 6 1
1 2 3
1 3 1
4 1 2
4 2 2
3 2 1
3 4 1
3
最小树形图中包含第2，5，6三边,总权值为1+1+1=3
样例2:输入-输出-解释
4 6 3
1 2 3
1 3 1
4 1 2
4 2 2
3 2 1
3 4 1
4
最小树形图中包含第3，5，6三边,总权值为2+1+1=4
样例3:输入-输出-解释
4 6 2
1 2 3
1 3 1
4 1 2
4 2 2
3 2 1
3 4 1
-1
无法构成最小树形图，故输出-1。
"""
def minWay(src:int,edges:list,total:int):
    weights = {}
    weights[src] = 0
    totalweight = 0
    while len(weights) != total:
        # print(weights)
        #选择最短的边
        minWeight = 2**31-1
        i = 0
        newVertice = -1
        while i < len(edges):
            headAdded = edges[i][0] in weights
            tailAdded = edges[i][1] in weights
            #如果尾部已经可达了就删掉
            if tailAdded:
                del edges[i]
                i -= 1
            elif headAdded:
                if edges[i][2] + weights[edges[i][0]] < minWeight:
                    minWeight = edges[i][2] + weights[edges[i][0]]
                    newVertice = edges[i][1]
            i += 1
        if newVertice == -1:
            print(-1)
            return
        else:
            weights[newVertice] = minWeight
            totalweight += minWeight
    print(totalweight)

if __name__ == "__main__":
    n,m,src = map(int,input().split())
    edges = []
    for i in range(m):
        edge = []
        s,t,w = map(int,input().split())
        edge.append(s)
        edge.append(t)
        edge.append(w)
        edges.append(edge)
    minWay(src,edges,n)