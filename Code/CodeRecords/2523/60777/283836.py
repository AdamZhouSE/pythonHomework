temp=input()
temp=temp[1:len(temp)-1]
i=1
j=0
mat=[]
while(i<len(temp)):
    while(temp[j]!=']'):
        j+=1
    n=temp[i:j]
    l=[int(x) for x in n.split(',')]
    mat.append(l)
    i=j+3
    j=i
def so(i,j):
    x=i
    y=j
    num=min(len(mat)-i,len(mat[0])-j)
    for m in range(num-1):
        x=i
        y=j
        while(x<len(mat)-1 and y<len(mat[0])-1):
            if(mat[x+1][y+1]<mat[x][y]):
                ex=mat[x][y]
                mat[x][y]=mat[x+1][y+1]
                mat[x+1][y+1]=ex
            x+=1
            y+=1
for i in range(len(mat[0])):
    so(0,i)
for j in range(1,len(mat)):
    so(j,0)
print(mat)
    