flag=[]
def deep(cx,cy,temp):
    if(cx==0):
        flag[0]=True
        return
    if(cx+1 in range(rn)):
        if(temp[cx+1][cy]==1):
            cm=temp.copy()
            cm[cx][cy]=0
            deep(cx+1,cy,cm)
    if(cx-1 in range(rn)):
        if(temp[cx-1][cy]==1):
            cm=temp.copy()
            cm[cx][cy]=0
            deep(cx-1,cy,cm)
    if(cy+1 in range(cn)):
        if(temp[cx][cy+1]==1):
            cm=temp.copy()
            cm[cx][cy]=0
            deep(cx,cy+1,cm)
    if(cy-1 in range(cn)):
        if(temp[cx][cy-1]==1):
            cm=temp.copy()
            cm[cx][cy]=0
            deep(cx,cy-1,cm)
    return
    
matrix=eval(input())
out=[]
rn=len(matrix)
cn=len(matrix[0])
drop=eval(input())
for item in drop:
    temp=matrix.copy()
    temp[item[0]][item[1]]=0
    count=0
    for i in range(rn):
        for j in range(cn):
            if(temp[i][j]==1):
                flag=[False]
                deep(i,j,temp)
                if(not flag[0]):
                    count+=1
    out.append(count)
print(out)