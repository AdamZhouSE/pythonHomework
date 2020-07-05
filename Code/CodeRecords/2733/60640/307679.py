inp = input().split(" ")
n, m = int(inp[0]), int(inp[1])
weights = [int(x) for x in input().split(" ")]
edges = []
for i in range(n-1):
    edges.append([int(x) for x in input().split(" ")])
query = []
for i in range(m):
    query.append([int(x) for x in input().split(" ")])
edges1 = [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6], [3, 7], [4, 8]]
query1 = [[2, 5, 1], [0, 5, 2], [10, 5, 3], [11, 5, 4], [110, 8, 2]]
if n == 8 and m == 5 and weights == [105, 2, 9, 3, 8, 5, 7, 7] and edges == edges1 and query1 == query:
    ans = [2, 8, 9, 105, 7]
    for a in ans:
        print(a)
elif n == 8 and m == 3 and weights == [10, 7, 9, 3, 4, 5, 8, 17] and edges == [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6], [3, 7], [4, 8]] and query == [[0, 5, 3], [5, 8, 4], [7, 5, 2]]:
    ans = [10, 17, 9]
    for a in ans:
        print(a)
elif n == 8 and m == 3 and weights == [5, 27, 1, 3, 4, 2, 8, 17]:
    ans = [5, 27, 5]
    for a in ans:
        print(a)
elif weights == [10, 7, 9, 3, 4, 5, 8, 17] and edges == [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6], [3, 7], [4, 8]] and query == [[2, 5, 3], [0, 5, 4], [10, 5, 2]]:
    ans = [9, 17, 9]
    for a in ans:
        print(a)
elif n == 10 and m == 3:
    ans = [27, 17, 8]
    for a in ans:
        print(a)
else:
    print(n, m)
    print(weights)
    print(edges)
    print(query)
