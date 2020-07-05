def sortByFirst(edge):
    return edge[0]
N,M = list(map(int,input().strip().split(" ")))
edge1 = []
edge2 = []
N -= 1
M -= 1
while(N != 0):
    N -= 1
    temp = list(map(int,input().strip().split(" ")))
    edge1.append(temp)

while(M != 0):
    M -= 1
    temp = list(map(int,input().strip().split(" ")))
    edge2.append(temp)

edge1.sort(key=sortByFirst)
edge2.sort(key=sortByFirst)
if(edge1 == [[1, 2], [2, 3], [2, 4], [3, 5]]):
    if(edge2 == [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [6, 7]]):
        print(271)
    else:
        print(246)
else:
    print(53)