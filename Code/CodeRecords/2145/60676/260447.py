def max_rectangle(graph):
    res = 0
    for k in range(1, len(graph)+1):
        for i in range(len(graph)-k+1):
            width = min(graph[i:i+k])
            length = k
            if width * length > res:
                res = width * length
    return res


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        a = input()
        g = input().split()
        for j in range(int(a)):
            g[j] = int(g[j])
        result.append(max_rectangle(g))
    for i in range(len(result)):
        print(result[i])