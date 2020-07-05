# 给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。
# 如果有多个目标子集，返回其中任何一个均可。


def fun(arr):
    # 有向图
    arr.sort()
    graph = [[] for i in range(len(arr))]
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] % arr[i] == 0:
                graph[j].append(i)
    length = []
    for i in range(len(arr)):
        if len(graph[i]) == 0:
            length.append(1)
        else:
            max_len = 1
            for j in range(len(graph[i])):
                if length[graph[i][j]] > max_len:
                    max_len = length[graph[i][j]]
            length.append(max_len + 1)
    max_index = 0
    for i in range(1, len(arr)):
        if length[i] > length[max_index]:
            max_index = i
    res = []
    while length[max_index] > 1:
        res.insert(0, arr[max_index])
        next_index = graph[max_index][0]
        for i in range(1, len(graph[max_index])):
            if length[graph[max_index][i]] > length[next_index]:
                next_index = graph[max_index][i]
        max_index = next_index
    res.insert(0, arr[max_index])
    return res


array = input().split(',')
for i in range(len(array)):
    array[i] = int(array[i])
print(fun(array))