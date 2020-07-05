# d[i][j] = min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+(s1[i] == s2[j]?0:1));
# 动态规划
def cal(first,second):
    l1 = len(first)
    l2 = len(second)
    if l1 == 0:
        return l2
    if l2 == 0:
        return l1
    graph = [([0] * l2) for i in range(l1)]
    for i in range(l1):
        graph[i][0] = i
    for i in range(l2):
        graph[0][i] = i
    for i in range(1,l1):
        for j in range(1,l2):
            if first[i] == second[j]:
                graph[i][j] = graph[i-1][j-1]
            else:
                graph[i][j] = min(graph[i-1][j]+1,graph[i][j-1]+1,graph[i-1][j-1]+1)
    return graph[l1-1][l2-1]

first = input()
second = input()
print(cal(first,second)+1) if first[0]!=second[0] else print(cal(first,second)) #由于在初始化graph的时候，（0，0）位置初始化是1，是默认第一位相同的

