def xor_calculate(f: int):
    for i in graph[f]:
        xor[i] = powers[f][i] ^ xor[f]
        graph[i].remove(f)
        xor_calculate(i)
    graph[f].clear()


if __name__ == '__main__':
    n = eval(input())
    graph = [[] for i in range(n)]
    powers = [[0 for j in range(n)] for i in range(n)]
    xor = [0 for i in range(n)]
    for i in range(n - 1):
        edge = input().split()
        graph[int(edge[0]) - 1].append(int(edge[1]) - 1)
        graph[int(edge[1]) - 1].append(int(edge[0]) - 1)
        powers[int(edge[0]) - 1][int(edge[1]) - 1] = int(edge[2])
        powers[int(edge[1]) - 1][int(edge[0]) - 1] = int(edge[2])
    xor_calculate(0)
    res = []
    for i in range(int(input())):
        check = input().split()
        res.append(xor[int(check[0]) - 1] ^ xor[int(check[1]) - 1])
    for i in res:
        print(i)