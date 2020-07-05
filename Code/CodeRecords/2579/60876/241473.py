import sys
width=int(input())
mat=[]
for i in range(0,width):
    mat.append(sys.stdin.readline().split(","))
target=int(input())
max=width
if len(mat[0])>width:
    max=len(mat[0])
jud=False
while max>0:
    for i in range(0,width-max+1):
        for j in range(0,len(mat[0])-max+1):
            sum=0
            for k in range(0,max):
                for t in range(0,max):
                    sum+=int(mat[i+k][j+t])
            if sum<=target:
                print(max)
                jud=True
                break
        if jud:
            break
    if jud:
        break
    else:
        max-=1
if max==0:
    print(0)

