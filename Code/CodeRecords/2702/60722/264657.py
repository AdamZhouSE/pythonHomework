world=[]
count=0
def DFS(i,j):
    if i<0 or j<0 or i>=4 or j>=5:
        return
    if world[i][j]=="1":
        world[i][j]="0"
        DFS(i-1,j)
        DFS(i+1,j)
        DFS(i, j-1)
        DFS(i, j+1)


for i in range(4):
    string=input()
    s=[]
    for j in range(len(string)):
        s.append(string[j])
    world.append(s)
for i in range(len(world)):
    for j in range(len(world[0])):
        if world[i][j]=="1":
            count+=1
            DFS(i,j)
print(count)