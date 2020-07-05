import queue


def bfs(adj, start):
    visited = set()
    order = []
    q = queue.Queue()
    q.put(start)
    visited.add(start)
    while not q.empty():
        u = q.get()
        order.append(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)
    return order


if __name__ == "__main__":
    turn = int(input())
    while turn > 0:
        cond = input().split( )
        num = int(cond[0])
        start = cond[1]
        nodes = input().split( )
        graph = {}
        for i in range(0, num):
            s = input().split( )
            son = []
            for j in range(1, len(s)):
                if int(s[j]) == 1:
                    son.append(nodes[j-1])
            graph[nodes[i]] = son
        order = bfs(graph, start)
        print(' '.join(order))
        turn -= 1
