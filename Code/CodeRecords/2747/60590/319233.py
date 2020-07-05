import sys
def init(edge, dictionary):  #初始化图
    for i in range(len(dictionary)):
        for j in range(i, len(dictionary)):
            if isable(dictionary[i], dictionary[j]):
                edge[i][j] = 1
                edge[j][i] = 1


def isable(word1, word2):  #只有一位不同就可以转化
    cnt = 0
    for i in range(len(word1)):
        if (word1[i] != word2[i]):
            cnt += 1
    if (cnt == 1):
        return True
    else:
        return False

def dijkstra(edge,start,dist): #记录从start到图中其它顶点的最短距离
    visited = [0]*len(edge)  #找到到u的最短路径是将visited[u]置1
    path = [-1]*len(edge)  #path[u]记录到u的前一个顶点
    for i in range(0,len(edge)):
        dist[i] = edge[start][i]
        if(dist[i]!=MAX_NUM and start!=i):
            path[i] = start
    visited[start] = 1
    dist[start] = 0
    for i in range(len(edge)):
        min = MAX_NUM
        end = start
        for j in range(len(edge)):
            if(visited[j]!=1 and dist[j]<min):
                min = dist[j]
                end = j
        visited[end] = 1
        for x in range(len(edge)):
            if(visited[x]!=1 and edge[end][x]<MAX_NUM and edge[end][x]+dist[end]<dist[x]):
                dist[x] = edge[end][x] + dist[end]
                path[x] = end

def getAllNeighbors(target,edge):
    res = []
    for i in range(len(edge)):
        if(edge[target][i])==1:
            res.append(i)
    return res

def ans(start,length):
    res = []
    if(length==0):
        return res.append(start)
    else:
        temp = getAllNeighbors(start,edge)
        for t in temp:
            res1 = []
            res1.append(start)
            res1 += ans(t,length-1)

MAX_NUM = sys.maxsize
startWord = input()
endWord = input()
dictionary = eval(input())
dictionary.append(startWord)
start = -1
end = -1
for i in range(len(dictionary)):
    if(dictionary[i]==startWord):
        start = i
    if(dictionary[i]==endWord):
        end = i
if(end==-1):
    print([])
else:
    edge = [[MAX_NUM] * len(dictionary) for i in range(len(dictionary))]
    dist = [0]*len(dictionary)
    init(edge,dictionary)
    dijkstra(edge,start,dist)
    minLen = dist[end]
    print(minLen)
    temp = ans(start,minLen)
    print(temp)