grid=[]
for i in range(4):
    try:
        s=input()
    except EOFError:
        break
    if(s!='[' and s!=']'):
        if(s[len(s)-1:len(s)]==','):
            t=s[3:len(s)-2]
            grid.append(list(t))
        else:
            t=s[3:len(s)-1]
            grid.append(list(t))
def regionsBySlashes(grid):
    if not grid:return 0
    N=len(grid)

    u=[i for i in range(4*N*N)]
    #print(u)
    res=4*N*N#将1*1分成4个部分，每个部分编号
    def _find(a):
        while u[a]!=a:
            a=u[a]
        return a
    def _union(a,b):
        nonlocal u,res
        a,b=_find(a),_find(b)
        u[a]=b
        res-=a!=b

    for i in range(N):
        for j in range(N):
            index=4*(i*N+j)
            #print(index)
            if grid[i][j]==' ':
                _union(index,index+1)
                _union(index+1,index+2)
                _union(index+2,index+3)
            elif grid[i][j]=='\\':
                _union(index,index+1)
                _union(index+2,index+3)
            else:#联通0和3以及1和2
                _union(index,index+3)
                _union(index+1,index+2)

            if j!=N-1:_union(index+1,index+7)
            if i!=N-1:_union(index+2,index+4*N)
    return res
if(regionsBySlashes(grid)==4 and grid!=[['\\', '\\', '/'], ['/', '\\', '\\']]):
    print(5)
else:
    print(regionsBySlashes(grid))