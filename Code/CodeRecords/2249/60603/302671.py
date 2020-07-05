def squar(N,info):
    XOY=0
    for i in info:
        for j in i:
            if j!=0:
                XOY=XOY+1
    XOZ=0
    for k in range(N):
        XOZ=XOZ+max(info[k])
    YOZ=0
    for m in range(N):
        a=[]
        for n in range(N):
            a.append(info[n][m])
        YOZ=YOZ+max(a)
    res=XOY+XOZ+YOZ
    print(res)
info=[]
N=int(input())
for b in range(N):
    inf=input().split(',')
    info.append([int(y) for y in inf])
squar(N,info)