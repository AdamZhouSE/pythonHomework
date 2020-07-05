if __name__ == "__main__":
    n,m = map(int,input().split(" "))
    edges = []
    totalweight = 0
    for i in range(m):
        a,b,w = map(int,input().split(" "))
        edges.append([a,b,w])
        totalweight += w
    added = [1]
    minindex = 0
    for i in range(n-1):
        minval = 2 ** 31 - 1
        j = 0
        while j < len(edges):
            if (edges[j][0] in added) and (edges[j][1] in added):
                del edges[j]
                j -= 1
            elif (not edges[j][0] in added) and (not edges[j][1] in added):
                j+=1
                continue
            #一个顶点在树里面
            else:
                if edges[j][2] < minval:
                    minval = edges[j][2]
                    minindex = j
            j += 1

        totalweight -= minval
        if edges[minindex][0] in added:
            added.append(edges[minindex][1])
        else:
            added.append(edges[minindex ][0])
        del edges[minindex]
    print(totalweight,end="")