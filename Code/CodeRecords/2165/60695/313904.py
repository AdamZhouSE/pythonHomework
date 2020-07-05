t = int(input())
for i in range(t):
    nstart = input().split(" ")
    n, start = int(nstart[0]), nstart[1]
    name = input().split(" ")
    v = {}
    a = []
    for j in range(n):
        t = input()[2:].split(" ")
        a.append(t)
        v[name[j]] = 0
    v[start] = 1
    index = name.index(start)
    edges = []
    for j in range(n):
        temp = a[index % n]
        edges.append(temp)
        index += 1
    print(start, end="")
    for j in range(n):
        for k in range(n):
            if edges[j][k] == '1' and v[name[k]] == 0:
                v[name[k]]=1
                print(" "+name[k], end="")
    print()
