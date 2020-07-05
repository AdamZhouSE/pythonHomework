class Edge(object):
    def __init__(self):
        self.f = 0
        self.s = 0
        self.w = 0


def find(x: int) -> int:
    if x == union_set[x]:
        return x
    else:
        union_set[x] = find(union_set[x])
        return union_set[x]


def krustal() -> int:
    ans = 0
    count = 0
    for i in range(e):
        f = find(edges[i].f)
        s = find(edges[i].s)
        if f == s:
            continue
        else:
            union_set[s] = union_set[f]
            ans += edges[i].w
            count += 1
            if count == n - 1:
                break
    return ans


if __name__ == '__main__':
    temp1 = input().split(' ')
    temp1 = list(map(int, temp1))
    n, e = temp1[0], temp1[1]
    edges = [Edge() for _ in range(e)]
    union_set = [i for i in range(n+1)]
    total_w = 0
    for i in range(e):
        temp2 = input().split(' ')
        temp2 = list(map(int, temp2))
        total_w += temp2[2]
        edges[i].f, edges[i].s, edges[i].w = temp2[0], temp2[1], temp2[2]
    edges.sort(key=lambda edge: edge.w)
    s = krustal()
    print(total_w - s)