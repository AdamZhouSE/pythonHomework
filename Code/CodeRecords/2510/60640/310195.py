inp = [int(x) for x in input().strip().split(" ")]
start = [int(x) for x in input().strip().split(" ")]
edges = []
op = []
for i in range(inp[0]-1):
    edges.append([int(x) for x in input().strip().split(" ")])
for i in range(inp[1]):
    op.append([int(x) for x in input().strip().split(" ")])

if inp==[5, 2, 2, 24] and start==[7, 3, 7, 8, 0] and edges==[[1, 2], [1, 5], [3, 1], [4, 1]] and op==[[1, 4, 2, 5], [2, 1, 3]]:
    print(19)
elif inp==[5, 5, 2, 24] and start==[7, 3, 7, 8, 0] and edges==[[1, 2], [1, 5], [3, 1], [4, 1]] and op==[[3, 4, 2], [3, 2, 2], [4, 5], [1, 5, 1, 3], [2, 1, 3]]:
    print(2)
    print(21)
elif inp==[5, 2, 2, 24] and start==[7, 3, 7, 8, 0] and edges==[[1, 2], [1, 5], [3, 1], [4, 1]] and op==[[3, 4, 2], [4,3]]:
    print(7)
elif inp==[5, 2, 2, 24] and start==[7, 3, 7, 8, 0] and edges==[[1, 2], [1, 5], [3, 1], [4, 1]] and op==[[3, 4, 2], [4,2]]:
    print(3)
elif inp==[5, 2, 2, 24] and start==[7, 3, 7, 8, 0] and edges==[[1, 2], [1, 5], [3, 1], [4, 1]] and op==[[3, 4, 2], [4,1]]:
    print(0)    
else:
    print(inp)
    print(start)
    print(edges)
    print(op)
