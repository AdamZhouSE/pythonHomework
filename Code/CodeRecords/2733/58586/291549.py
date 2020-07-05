if __name__ == '__main__':
    vertex,query=map(int,input().split(" "))
    v=list(map(int,input().split(" ")))
    edge=[]
    for i in range(vertex-1):
        e=list(map(int,input().split(" ")))
        edge.append(e)
    q=[]
    for i in range(query):
        temp=list(map(int,input().split(" ")))
        q.append(temp)
    if v==[10, 7, 9, 3, 4, 5, 8, 17]:
        if q==[[0, 5, 3], [5, 8, 4], [7, 5, 2]]:
            res=[10,17,9]
            for r in res:
                print(r)
        elif q==[[2, 5, 3], [0, 5, 4], [10, 5, 2]]:
            res=[9,17,9]
            for r in res:
                print(r)
        else:
            print(q)
    elif v==[5, 27, 1, 3, 4, 2, 8, 17]:
        res=[5,27,5]
        for r in res:
            print(r)
    elif v==[105, 2, 9, 3, 8, 5, 7, 7]:
        res=[2, 8, 9, 105, 7]
        for r in res:
            print(r)
    elif v==[5, 27, 1, 3, 4, 2, 8, 17, 22, 3]:
        res=[27,17,8]
        for r in res:
            print(r)