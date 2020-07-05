N = int(input())
edges = []
for a in range(0,N-1):
    row = input().split(' ')
    for b in range(0,len(row)):
        row[b] = int(row[b])
    edges.append(row)
M = int(input())
for a in range(0,M):
    row = input().split(' ')
    start = int(row[0])
    end = int(row[1])
    k = 0
    while start!=end:
        for i in edges:
            if i[0]==start:
                start = i[1]
                k = k^i[2]
                break
    print(k)
