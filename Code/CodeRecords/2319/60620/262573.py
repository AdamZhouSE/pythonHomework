n=int(input())
r=[]
for i in range(n):
    a=list(map(int,input().split(',')))
    r.extend([a])
num=0
lx=len(r)
ly=len(r[0])
x,y,z=0,0,0
for i in range(lx):
    for j in range(ly):
        if(r[i][j]==0):
            continue
        num+=r[i][j]
        z+=r[i][j]-1
        if(i+1<lx and r[i+1][j]>0):
            x+=min(r[i][j],r[i+1][j])
        if(j+1<ly and r[i][j+1]>0):
            y+=min(r[i][j],r[i][j+1])
print(6*num-2*(x+y+z))

    