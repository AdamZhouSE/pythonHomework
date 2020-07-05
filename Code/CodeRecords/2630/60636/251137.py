def location(source,a):
    for i in len(source):
        for j in len(source[0]-1):
            if(source[i][j]==a):
                return [i,j]
def find(source,i,j,alls):
    if i==0 and j==0:
        return min([source[0][1],source[1][0]])
    elif i==0 and j==len(source[i])-1:
        if(not location(alls,min([source[0][j-1],source[1][j]])) in alls):
            return min([source[0][j-1],source[1,j]])
    elif j==0 and i==len(source)-1:
        if(not location(alls,min([source[i-1][0],source[i][1]])) in alls):
            return min([source[i-1][0],source[i][1]])
    elif i==0:
        if(not location(alls,min([source[i][j-1],source[i][j+1],source[i+1][j]])) in alls):
            return min([source[i][j-1],source[i][j+1],source[i+1][j]])
    elif j==0:
        if(not location(alls,min([source[i-1][j],source[i+1][j],source[i][j+1]])) in alls):
            return min([source[i-1][j],source[i+1][j],source[i][j+1]])
    elif i==len(source)-1:
        if(not location(alls,min([source[i-1][j],source[i][j-1],source[i][j+1]])) in alls):
            return min([source[i-1][j],source[i][j-1],source[i][j+1]])
    elif j==len(source[0])-1:
        if(not location(alls,min([source[i-1][j],source[i+1][j],source[i][j-1]])) in alls):
            return min([source[i-1][j],source[i+1][j],source[i][j-1]])
    else:
        if(not location(alls,min([source[i-1][j],source[i+1][j],source[i][j-1],source[i][j+1]])) in alls):
            return min([source[i-1][j],source[i+1][j],source[i][j-1],source[i][j+1]])
        
grid=eval(input())
alls=[]
alls.append([0,0])
result=[]
result.append(grid[0][0])
while(True):
    possiable=[]
    print(alls)
    for a in alls:
        possiable.append(find(grid,a[0],a[1],alls))
    result.append(min(possiable))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] in possiable):
                alls.append([i,j])
    if(grid[len(grid)-1][len(grid[0])-1] in result):
        break
print(resullt)
















    