def min_node(queue,rest,edges):
    while rest!=1 and rest!=2:
        size=len(queue)
        rest-=size
        for i in range(size):
            front=queue.pop()
            for e in edges[front]:
                degrees[e]-=1
                if degrees[e]==1:
                    queue.insert(0,e)
    return queue


if __name__ == '__main__':
    n = int(input())
    src = eval(input())
    edges=[]
    for i in range(n):
        edges.append([])

    degrees=[0]*n

    for e in src:
        edges[e[0]].append(e[1])
        edges[e[1]].append(e[0])
        degrees[e[0]]+=1
        degrees[e[1]]+=1

    queue=[]
    rest=n
    if rest==1:
        print(0)
    else:
        for i in range(n):
            if degrees[i]==1:
                queue.insert(0,i)
        print(sorted(min_node(queue,rest,edges)))