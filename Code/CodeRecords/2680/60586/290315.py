def exam17():
    T=int(input())
    for t in range(T):
        x=input().split(" ")
        a=int(x[0])
        b=int(x[1])
        n=1
        mtri=[]
        for i in range(a):
            mtri.append([])
            for j in range(b):
                mtri[i].append(0)
        for i in range(a):
            for j in range(b):
                if i==0 or j==0:
                    mtri[i][j]=1
                else:
                    mtri[i][j]=mtri[i][j-1]+mtri[i-1][j]
        print(mtri[a-1][b-1])
exam17()