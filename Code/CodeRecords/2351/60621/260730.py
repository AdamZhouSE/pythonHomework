a=eval(input())

grid=[[0 for i in range(a)] for j in range(a)]
for i in range(a-1):
    trmp=[int(x)-1 for x in input().split()]
    grid[trmp[0]][trmp[1]]=1
    grid[trmp[1]][trmp[0]]=1
maximum=0
union=[True for i in range(a)]
clue=[0 for i in range(a)]#remember the largest number
#union recorded the node we have visited
def dp(i,ban,path:list):
    global maximum
    union[i]=False
    maximum+=1
    path.append(i)
    for j in range(a):
        if j!=ban and grid[i][j]==1 and j not in path:
            dp(j,ban,path)

    path.pop()

for i in range(a):
    ban=i
    union = [True for i in range(a)]
    for j in range(a):

        maximum=0
        if union[j] and j!=i:
            dp(j,ban,[])
        clue[ban]=max(clue[ban],maximum)
godfather=[]
ma=a
for i in range(a):
    if clue[i]<ma:
        ma=clue[i]
        godfather=[i]
    elif clue[i]==ma:
        godfather.append(i)
for i in godfather:
    print(i+1,end=" ")