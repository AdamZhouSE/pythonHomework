def location(source,a):
    for i in range(len(source)):
        for j in range(len(source[0])-1):
            if(source[i][j]==a):
                return [i,j]
def find(source,i,j,alls):
    if i==0 and j==0:
        return min([source[0][1],source[1][0]])
    elif i==0 and j==len(source[i])-1:
        a=[source[0][j-1],source[1][j]]
        y=a.copy()
        for x in a:
            if(location(source,x) in alls):
                y.pop(y.index(x))
        if(not min(y) in alls):
            return min(y)
    elif j==0 and i==len(source)-1:
        a=[source[i-1][0],source[i][1]]
        y=a.copy()
        for x in a:
            if(location(source,x) in alls):
                y.pop(y.index(x))
        if(not min(y) in alls):
            return min(y)
    elif i==0:
        a=[source[i][j-1],source[i][j+1],source[i+1][j]]
        y=a.copy()
        for x in a:
            if(location(source,x) in alls):
                y.pop(y.index(x))
        if(not min(y) in alls):
            return min(y)
    elif j==0:
        a=[source[i-1][j],source[i+1][j],source[i][j+1]]
        y=a.copy()
        for x in a:
            if(location(source,x) in alls):
                y.pop(y.index(x))
        if(not min(y) in alls):
            return min(y)
    elif i==len(source)-1:
        a=[source[i-1][j],source[i][j-1],source[i][j+1]]
        y=a.copy()
        for x in a:
            if(location(source,x) in alls):
                y.pop(y.index(x))
        if(not min(y) in alls):
            return min(y)
    elif j==len(source[0])-1:
        a=[source[i-1][j],source[i+1][j],source[i][j-1]]
        y=a.copy()
        for x in a:
            if(location(source,x) in alls):
                y.pop(y.index(x))
        if(not min(y) in alls):
            return min(y)
    else:
        a=[source[i-1][j],source[i+1][j],source[i][j-1],source[i][j+1]]
        y=a.copy()
        for x in a:
            if(location(source,x) in alls):
                y.pop(y.index(x))
        if(not min(y) in alls):
            return min(y)
        
grid=eval(input())
alls=[]
alls.append([0,0])
result=[]
result.append(grid[0][0])
while(True):
    possiable=[]
    print(result)

    for a in alls:
        if(find(grid,a[0],a[1],alls)!=None):
            possiable.append(find(grid,a[0],a[1],alls))
    print(possiable)
    result.append(min(possiable))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] in possiable):
                alls.append([i,j])
    print(alls)
    if(grid[len(grid)-1][len(grid[0])-1] in result):
        break
print(resullt)
















    