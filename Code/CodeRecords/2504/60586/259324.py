def exam5():
    X = list(input())
    points=[]
    dis=[]
    seq=[]
    X.remove(",")
    X.remove("[")
    X.remove("]")
    for i in range(len(X)):
        if X[i]=="-":
            points.append(int(X[i]+X[i+1]))
            i=i+1
        else:
            points.append(int(X[i]))
    for i in range(0,len(points),2):
        dis.append(2**points[i]+2**points[i+1])
    k=int(input())
    dis.sort()
    for j in range(k):
        for i in range(0, len(points), 2):
            if 2**points[i]+2**points[i+1]==dis[k]:
                seq.append("[{},{}]".format(points[i],points[i+1]))
    print(seq)
exam5()