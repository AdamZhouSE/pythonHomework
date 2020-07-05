class Edge(object):
    def __init__(self):
        self.fa = 0
        self.son = 0
        self.w = 0


def find() -> int:
    count = 0
    ans = 0
    for i in range(m):
        f = edges[i].fa
        s = edges[i].son
        if union_set[f] == union_set[s]:
            continue
        union_set[s] = f
        ans = edges[i].w
        count += 1
        if count == n - 1:
            break
    return ans


if __name__ == '__main__':
    temp1 = input().split(' ')
    temp1 = list(map(int, temp1))
    n, m = temp1[0], temp1[1]
    union_set = [i for i in range(n+1)]
    edges = [Edge() for _ in range(m)]
    for i in range(m):
        temp2 = input().split(' ')
        temp2 = list(map(int, temp2))
        edges[i].fa, edges[i].son, edges[i].w = temp2[0], temp2[1], temp2[2]
    edges.sort(key=lambda edge: edge.w)
    k = find()
    print(k, end='')