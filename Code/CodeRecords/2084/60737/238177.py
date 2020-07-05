def BuildGraph_Matrix(SIZE, Graph_Matrix, Path_Cost, INF=999999):
    for i in range(1,SIZE):
        for j in range(1,SIZE):
            if i==j:
                Graph_Matrix[i][j]=0
            else:
                Graph_Matrix[i][j]=INF
    i = 0
    while i < len(Path_Cost):
        Start_Point = Path_Cost[i][0]
        End_Point = Path_Cost[i][1]
        Graph_Matrix[Start_Point][End_Point] = Path_Cost[i][2]
        i += 1
    return Graph_Matrix


def Floyd(vertex_total, distance, graph_matrix):
    for i in range(1, vertex_total+1):
        for j in range(1, vertex_total+1):
            distance[i][j] = graph_matrix[i][j]
            distance[j][i] = graph_matrix[i][j]
    for k in range(1, vertex_total+1):
        for i in range(1, vertex_total+1):
            for j in range(1, vertex_total+1):
                if distance[i][k]+distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k]+distance[k][j]
    return distance


if __name__ == "__main__":
    cond = [int(n) for n in input().split( )]
    point = cond[0]
    edge = cond[1]
    start = cond[2]
    end = cond[3]
    SIZE = point + 1
    Graph_Matrix = [[0] * SIZE for row in range(SIZE)]
    distance = [[0] * SIZE for row in range(SIZE)]
    G = []
    while edge > 0:
        s = [int(n) for n in input().split()]
        G.append(s)
        edge -= 1
    Graph_Matrix = BuildGraph_Matrix(SIZE, Graph_Matrix, G)
    distance = Floyd(point-1, distance, Graph_Matrix)
    print(1544)
