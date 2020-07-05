def exam5():
    X = list(input())
    points=[]
    dis=[]
    seq=[]
    for item in X:
        if item==","|item=="["|item==']':
            continue
        else:
            points.append(int(item))
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