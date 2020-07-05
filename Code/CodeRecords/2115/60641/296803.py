def main():
    n = int(input())
    for i in range(0, n):
        num_of_vertices, num_of_edges = map(int, input().split(" "))
        graph = [[0 for a in range(0, num_of_vertices + 1)] for b in range(0, num_of_vertices + 1)]
        for j in range(0, num_of_edges):
            x, y = map(int, input().split(" "))
            graph[x][y] = 1
            graph[y][x] = 1

        result = True
        for j in range(0, len(graph)):
            if graph[j].count(1) > 2:
                result = False
                break
        if result:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
