length=int(input())
grids=[]
for i in range(length):
    row=input().split(',')
    row=list(map(int,row))
    grids.append(row)
xoy=0
yoz=0
xoz=0
for i in range(length):
    highest_1=0
    highest_2=0
    for j in range(length):
        if grids[i][j]!=0:
            xoy+=1
        highest_1=max(highest_1,grids[i][j])
        highest_2=max(highest_2,grids[j][i])
    yoz+=highest_1
    xoz+=highest_2
print(xoz+xoy+yoz)