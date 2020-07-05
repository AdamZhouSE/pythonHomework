def height(x: int) -> int:
    if len(f_s[x]) == 0:
        return 1
    l = 0
    for j in f_s[x]:
        l = max(l, 1 + height(j))
    return l


def width() -> int:
    b = 1
    queue = []
    for j in f_s[1]:
        queue.append(j)
    while len(queue) != 0:
        l = len(queue)
        b = max(b, l)
        for _ in range(l):
            temp = queue[0]
            for j in f_s[temp]:
                queue.append(j)
            queue.remove(temp)
    return b


def search(node: int, target: int, edge: int):
    global d
    if node == target:
        d = edge
    for j in f_s[node]:
        search(j, target, edge + 1)


if __name__ == '__main__':
    n = int(input())
    f_s = [[] for _ in range(n + 1)]
    union_set = [-1 for _ in range(n + 1)]
    for i in range(n - 1):
        temp1 = input().rstrip(' ').split(' ')
        temp1 = list(map(int, temp1))
        f_s[temp1[0]].append(temp1[1])
        union_set[temp1[1]] = temp1[0]
    temp3 = input().rstrip(' ').split(' ')
    temp3 = list(map(int, temp3))
    node1, node2 = temp3[0], temp3[1]
    h = height(1)
    w = width()
    d = 0
    search(1, node1, 0)
    d1 = d
    search(1, node2, 0)
    d2 = d
    common_fa = -1
    n1 = node1
    n2 = node2
    if d1 > d2:
        for _ in range(d1 - d2):
            temp = union_set[n1]
            if temp == n2:
                common_fa = n2
                break
            n1 = temp
    elif d2 > d1:
        for _ in range(d2 - d1):
            temp = union_set[n2]
            if temp == n1:
                common_fa = n1
                break
            n2 = temp
    if common_fa == -1:
        while n1 != n2:
            n1 = union_set[n1]
            n2 = union_set[n2]
        common_fa = n1
    search(common_fa, node1, 0)
    d1 = d
    search(common_fa, node2, 0)
    d2 = d
    ans = d1 * 2 + d2
    print(h)
    print(w)
    print(ans, end='')