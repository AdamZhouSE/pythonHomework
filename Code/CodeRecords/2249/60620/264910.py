n=int(input())
r=[]
result=0
for i in range(n):
    a=list(map(int,input().split(',')))
    r.extend([a])
for i in range(len(r)):
    row=0
    col=0
    for j in range(len(r)):
        if(r[i][j]):
            result+=1
            row=max(row,r[i][j])
            col=max(col,r[j][i])
    result+=row+col
print(result)
