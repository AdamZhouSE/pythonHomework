m=[]
for i in range(3):
    m.append(list(map(int,input().split())))

result=[[0 for i in range(3)]for j in range(3)]


rn=3
cn=3


def deep(cx,cy,count):
    if(m[cx][cy]==0):
        out.append(count)
        return
    if count>min(out):
        return
    if cx+1 in range(3): 
       deep(cx+1,cy,count+1)
    if cx-1 in range(3): 
        deep(cx-1,cy,count+1)
    if cy+1 in range(3): 
        deep(cx,cy+1,count+1)
    if cy-1 in range(3): 
        deep(cx,cy-1,count+1)
    

for i in range(3):
    for j in range(3):
        out=[4]
        deep(i,j,0)
        result[i][j]=min(out)    
        
for i in range(3):
    for j in range(3):
        if j!=2:
            print(result[i][j],end=" ")
        elif i!=2:
            print(result[i][j])
        else:
            print(result[i][j])