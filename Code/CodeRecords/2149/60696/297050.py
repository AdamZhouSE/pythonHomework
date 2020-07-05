"""
寻找最大连通块
"""


def find(i: int, edges_now:list):
    connected_pieces.clear()
    vis = [False] * (n + 1)
    for t in range(1, n + 1):
        if vis[t]:
            continue
        if t == i:
            continue
        q = [t]
        temp = []
        while len(q) != 0:
            top = q.pop(0)
            vis[top] = True
            temp.append(top)
            for j in range(len(edges_now[top])):
                if vis[edges_now[top][j]]:
                    continue
                if q.__contains__(edges_now[top][j]):
                    continue
                if edges_now[top][j] == i:
                    continue
                q.append(edges_now[top][j])
        connected_pieces.append(temp)


if __name__ == '__main__':
    arr = [int(_) for _ in input().split()]
    n, k = arr[0], arr[1]
    edges = [[] for _ in range(n+1)]
    # edges = [[0] for _ in range(n + 1)]
    degree = [0] * (n+1)
    for i in range(n-1):
        arr = [int(_) for _ in input().split()]
        edges[arr[0]].append(arr[1])
        edges[arr[1]].append(arr[0])
        degree[arr[0]] += 1
        degree[arr[1]] += 1
    connected_pieces = []
    for i in range(1, n + 1):
        find(i, edges.copy())
        connected_pieces.sort(key=lambda x: len(x), reverse=True)
        if len(connected_pieces[0]) <= n / 2:
            print(1)
        else:
            cnt = k
            degree_now = degree.copy()
            for j in range(len(edges[i])):
                degree_now[edges[i][j]] -= 1
            temp = list(connected_pieces[0]).copy()
            temp.sort(key=lambda x: degree_now[x], reverse=True)
            if degree_now[temp[0]] - k + 1 <= n/2:
                print(1)
            else:
                print(0)