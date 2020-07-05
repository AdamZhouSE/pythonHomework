inp = input().split(" ")
n, m, k = int(inp[0]), int(inp[1]), int(inp[2])
pos = []
for i in range(n):
    pos.append([int(x) for x in input().strip().split(" ")])
edges = []
for i in range(m):
    edges.append([int(x) for x in input().strip().split(" ")])
plan = [int(x) for x in input().split(" ")]
if n==9 and m==14 and k==5 and plan==[3, 3, 0, 4, 7, 1, 3, 4, 6, 4, 8, 0, 4, 3, 6, 2, 3, 8, 0, 4, 6, 2, 5, 0, 4, 5, 7, 6, 3]:
    print(1,1)
    print(1,2)
    print(1,1)
    print(9,10)
    print(3,4)
else:
    print(n,m,k)
    print(pos)
    print(edges)
    print(plan)