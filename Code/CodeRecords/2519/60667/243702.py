edges = eval(input())
edges.sort(reverse=True)
for i in range(len(edges)-2):
    if edges[i] < edges[i+1] + edges[i+2]:
        print(edges[i] + edges[i+1] + edges[i+2])
        quit()
print(0)