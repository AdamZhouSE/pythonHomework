raw_str = input()
N = len(raw_str)

graph = [[] for i in range(N)]
for i in range(N):
    graph[i].append(i)


# Function to add edge
def add_edge(u, v):
    graph[u].append(v)
    graph[v].append(u)
    for item1 in graph[u]:
        for item2 in graph[v]:
            if item2 not in graph[item1]:
                graph[item1].append(item2)
                graph[item2].append(item1)


def link(pairs):
    for i in range(len(pairs)//2):
        u = int(pairs[i * 2][-1])
        v = int(pairs[i * 2 + 1][0])
        add_edge(u, v)


def sort_string(raw_str):
    # 未处理的下标列表
    index_list = []
    # 排序后的列表
    res = []
    # 初始化
    for i in range(N):
        index_list.append(i)
        res.append(raw_str[i])
        graph[i].sort()

    while len(index_list) > 0:
        sort_list = []
        temp = index_list[0]
        for item in graph[temp]:
            sort_list.append(raw_str[item])
        sort_list.sort()
        index = 0
        for item in graph[temp]:
            # 此处前提是图的每一个列表都已经排好序
            res[item] = sort_list[index]
            index_list.remove(item)
            index += 1

    new_str = ''
    for i in range(len(res)):
        new_str += res[i]
    return new_str


pairs = input().split(',')
link(pairs)
print(sort_string(raw_str))