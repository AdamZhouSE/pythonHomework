n=int(input())
mat=[]

for i in range(n):
    temp=[int(x) for x in input().split(',')]
    mat.append(temp)
    
thr=int(input())

add=0
getin=False
for i in range(max(len(mat),len(temp)),0,-1):
    getin=False
    for j in range(0,len(mat)-i+1):
        for k in range(0,len(temp)-i+1):
            add=0
            getin=True
            for x in range(0,i):
                for y in range(0,i):
                    add+=mat[j+x][k+y]
            if(add<=thr and getin):
                break
        if(add<=thr and getin):
            break
    if(add<=thr and getin):
        break

if(add>thr):
    i=0
print(i)
if(i==7):
    print(thr)
    print(mat)
