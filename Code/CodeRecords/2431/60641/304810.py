import math
import copy


def union(nums, num):
    past = nums[num]
    while past != -1:
        num = past
        past = nums[past]
    return num


if __name__ == '__main__':
    s, p = map(int, input().strip().split(" "))
    t = s
    xs = [0 for i in range(0, p)]
    ys = [0 for i in range(0, p)]
    for i in range(0, p):
        x, y = map(int, input().strip().split(" "))
        xs[i] = x
        ys[i] = y
    edges = []
    for i in range(0, p):
        for j in range(i + 1, p):
            length = round(math.sqrt((xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2), 2)
            edges.append([i, j, length])
    past = [-1 for i in range(0, p)]
    edges = sorted(edges, key=lambda x: x[2])
    tree_edges = []
    while len(tree_edges) != p - 1:
        edge = edges[0]
        if union(past, edge[0]) != union(past, edge[1]):
            past[edge[1]] = edge[0]
            tree_edges.append(edge)
        del edges[0]

    vertices = []
    tree_edges = sorted(tree_edges, key=lambda x: x[2], reverse=True)
    temp = copy.deepcopy(tree_edges)
    # for edge in temp:
    #     if s > 0:
    #         if s >= 2:
    #             if edge[0] not in vertices and edge[1] not in vertices:
    #                 vertices.append(edge[0])
    #                 vertices.append(edge[1])
    #                 s -= 2
    #                 tree_edges.remove(edge)
    #             elif edge[0] in vertices:
    #                 vertices.append(edge[1])
    #                 s -= 1
    #                 tree_edges.remove(edge)
    #             elif edges[1] in vertices:
    #                 vertices.append(edge[0])
    #                 s -= 1
    #                 tree_edges.remove(edge)
    #         else:
    #             if edge[0] in vertices and edge[1] not in vertices:
    #                 vertices.append(edge[1])
    #                 s -= 1
    #                 tree_edges.remove(edge)
    #             elif edge[1] in vertices and edge[0] not in vertices:
    #                 vertices.append(edge[0])
    #                 s -= 1
    #                 tree_edges.remove(edge)
    #     else:
    #         break
    print('%.2f' %(tree_edges[s - 1][2]), end="")
