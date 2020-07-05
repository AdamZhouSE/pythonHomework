t=int(input())
for i in range(t):
    ns=input().split(' ')
    n=int(ns[0])
    start=ns[1]
    visited=[]
    visited.append(start)
    nodes=input().split(' ')
    matrix=[]
    for j in range(n):
        row=input().split(' ')
        row.pop(0)
        matrix.append(row)
    queue=[]
    queue.append(start)
    while(len(queue)>0):
        v=queue.pop(0)
        neighbors=nodes[:]
        neighbors.sort()
        v_row=nodes.index(v)
        while len(neighbors)>0:
            next_neighbor=neighbors.pop(0)
            idx_nghnr=nodes.index(next_neighbor)
            if next_neighbor not in visited and matrix[v_row][idx_nghnr]=='1':
                visited.append(next_neighbor)
                queue.append(next_neighbor)
    print(' '.join(visited))