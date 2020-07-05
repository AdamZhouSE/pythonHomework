d=[]
try:
    while True:
        d.append(input())
        if(d[len(d)-1]=="]"):
            break
except EOFError:
    pass
a=[]
for i in d[1:len(d)-1]:
    a.append(eval(i.rstrip(",")))
position=[[-1,0],[0,1],[1,0],[0,-1]]
row,col=len(a),len(a[0])
valid=[]
best=[]
def check(x,y):
    if(x<0 or x>=row or y<0 or y>=col):
        return False
    else:
        return True
def dp(x,y,path:list):
    global best
    path.append(a[x][y])
    for i in range(4):
        xi=x+position[i][0]
        yi=y+position[i][1]
        if(check(xi,yi) and a[x][y]<a[xi][yi]):

            dp(xi,yi,path)

    if(len(path)>len(best)):
        best=[x for x in path]
    path.pop()
    return

for i in range(row):
    for j in range(col):
        dp(i,j,[])

print(len(best))
