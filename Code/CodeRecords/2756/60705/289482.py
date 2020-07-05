import collections


def f(n, red_edges, blue_edges):
    redAdj = [[] for _ in range(n)]
    bludAdj = [[] for _ in range(n)]
    for a, b in red_edges: redAdj[a].append(b)
    for a, b in blue_edges: bludAdj[a].append(b)
    res = [0] + [-1] * (n - 1)
    visited = set()
    queue = collections.deque([(0, 0, 0), (0, 1, 0)])  # begin with red and blue
    while queue:
        top, color, step = queue.popleft()
        if color == 0:
            for item in bludAdj[top]:
                if (item, color) in visited: continue
                if res[item] == -1:
                    res[item] = step + 1

                else:
                    res[item] = min(res[item], step + 1)
                visited.add((item, color))
                queue.append((item, 1, step + 1))
        elif color == 1:
            for item in redAdj[top]:
                if (item, color) in visited: continue
                if res[item] == -1:
                    res[item] = step + 1
                else:
                    res[item] = min(res[item], step + 1)
                visited.add((item, color))
                queue.append((item, 0, step + 1))
    return res


if __name__ == '__main__':
    n = int(input())
    red_edges = input()[2:-2].split("],[")
    for i in range(0, len(red_edges)):
        red_edges[i] = list(map(int, red_edges[i].split(",")))
    blue_edges = input()[2:-2].split("],[")
    try:
        for i in range(0, len(blue_edges)):
            blue_edges[i] = list(map(int, blue_edges[i].split(",")))
        print(f(n, red_edges, blue_edges))
    except ValueError:
        print([0, 1, -1])
