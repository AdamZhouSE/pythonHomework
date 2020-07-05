def find(source,i,j,alls):
    if i==0 and j==0:
        alls.append(source[0,0])
        alls.append(min(source[0,1],source[1,0]))
    elif i==0 and j==len(source[i])-1:
        if(not min(source[0][j-1],source[1][j]) in alls):
            alls.append(min(source[0][j-1],source[1,j]))
    elif j==0 and i==len(source)-1:
        if(not min(source[i-1][0],source[i][1]) in alls):
            alls.append(min(source[i-1][0],source[i][1]))
    elif i==0:
        if(not min([source[i][j-1],source[i][j+1],source[i+1][j]]) in alls):
            alls.append(min([source[i][j-1],source[i][j+1],source[i+1][j]]))
    elif j==0:
        if(not min([source[i-1][j],source[i+1][j],source[i][j+1]]) in alls):
            alls.append(min([source[i-1][j],source[i+1][j],source[i][j+1]]))
    elif i==len(source)-1:
        if(not min([source[i-1][j],source[i][j-1],source[i][j+1]]) in alls):
            alls.append(min([source[i-1][j],source[i][j-1],source[i][j+1]]))
    elif j==len(source[0])-1:
        if(not min([source[i-1][j],source[i+1][j],source[i][j-1]]) in alls):
            alls.append(min([source[i-1][j],source[i+1][j],source[i][j-1]]))
    else:
        if(not min([source[i-1][j],source[i+1][j],source[i][j-1],source[i][j+1]]) in alls):
            alls.append(min([source[i-1][j],source[i+1][j],source[i][j-1],source[i][j+1]]))
        
grid=eval(input())
target=findroad(grid)
targets=[]
for i in target:
    a=[]
    for j in i.split(" "):
        a.append(int(j))
    targets.append(a)
res=[]
for i in targets:
    res.append(max(i))
print(min(res))