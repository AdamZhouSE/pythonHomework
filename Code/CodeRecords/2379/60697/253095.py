k=input()
d=0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
x=0
y=0
for ins in k:
    if(ins=='R'):
        d+=1
    elif(ins=='L'):
        d+=3

    elif(ins=='G'):
        d=d%4
        x=x+dx[d]
        y=y+dy[d]

s="False"
if(x==0 and y==0):
    s="True"
if(d%4!=0):
    s="True"
print(s)