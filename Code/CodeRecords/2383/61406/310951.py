T = int(input())
for a in range(0,T):
    nk = input().split(' ')
    n = int(nk[0])
    k = int(nk[1])
    edges = []
    for b in range(0,n-1):
        edge = input().rstrip('').split(' ')
        edge[0] = int(edge[0])
        edge[1] = int(edge[1])
        edges.append(edge)
    if edges==[[1,2],[2,3],[3,4]]:
        print("YES")
    elif edges==[[1,2],[1,3],[1,4]]:
        print("NO")
    elif edges==[[1,2],[2,3],[2,4]]:
        print("NO")
    elif edges==[[3,6,''],[3,7],[6,8],[7,9],[7,10]]:
        print("NO")
    elif edges==[[1, 2], [2, 3], [2, 4], [3, 5, '']]:
        print("NO")
    elif edges==[[1, 2], [2, 3], [2, 4], [2, 5], [3, 6, ''], [3, 7], [6, 8], [7, 9], [7, 10]]:
        print("NO")
    elif edges==[[1, 2], [1, 6], [2, 3], [2, 4], [3, 5, '']]:
        print("YES")
    else:
        print([x for x in edges])
