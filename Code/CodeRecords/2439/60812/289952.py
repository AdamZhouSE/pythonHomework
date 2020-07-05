n = int(input())
tree = {i: [] for i in range(1, n+1)}
for i in range(n-1):
    u, v, weight = [int(i) for i in input().split(' ')]
    tree[v] = [u, weight]
M = int(input())
for i in range(M):
    u, v = [int(i) for i in input().split(' ')]
    weight = 0
    while u != v:
        temp = tree[v]
        weight ^= temp[1]
        v = temp[0]
    print(weight)
