land=eval(input())
rn=len(land)
cn=len(land[0])
c_0=False
c_1=False
for i in land:
    for j in i:
        if j==0:
            c_0=True
        if j==1:
            c_1=True

dis=[]
visited=[[0 for i in range(cn)]for i in range(rn)]
def deep(cx,cy,ix,iy,visited):
    hd=abs(cx-ix)+abs(cy-iy)
    if hd>min(dis):
        return
    if(land[cx][cy]==1):
        dis.append(hd)
    if cx+1 in range(rn) and visited[cx+1][cy]!=1:
        visited[cx+1][cy]=1
        deep(cx+1,cy,ix,iy,visited)
    if cx-1 in range(rn)and visited[cx-1][cy]!=1:
        visited[cx-1][cy]=1
        deep(cx-1,cy,ix,iy,visited)
    if cy+1 in range(cn)and visited[cx][cy+1]!=1:
        visited[cx][cy+1]=1
        deep(cx,cy+1,ix,iy,visited)
    if cy-1 in range(cn)and visited[cx][cy-1]!=1:
        visited[cx][cy-1]=1
        deep(cx,cy-1,ix,iy,visited)
out=[]
if c_0 and c_1:
    for i in range(rn):
        for j in range(cn):
            if land[i][j]==0:
                dis=[rn-1+cn-1]
                visited=[[0 for i in range(cn)]for i in range(rn)]
                deep(i,j,i,j,visited)
                out.append(min(dis))
    print(max(out))
else:
    print(-1)