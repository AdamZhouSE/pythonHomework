import copy
bricks=eval(input())
operations=eval(input())
m=len(bricks)
n=len(bricks[0])
record_topBricks=[[0]*n for i in range(m)]
for j in range(n):
    if(bricks[0][j]==1):
        record_topBricks[0][j]=1
stability=copy.deepcopy(record_topBricks)
def detect_stability(i,j):
    global stability,bricks
    if (i != 0):
        if (bricks[i - 1][j] == 1 and stability[i - 1][j] != 1):
            stability[i - 1][j] = 1
            detect_stability(i - 1, j)
    if (i != m-1):
        if (bricks[i + 1][j] == 1 and stability[i + 1][j] != 1):
            stability[i + 1][j] = 1
            detect_stability(i + 1, j)
    if (j != 0):
        if (bricks[i][j - 1] == 1 and stability[i][j - 1] != 1):
            stability[i][j - 1] = 1
            detect_stability(i, j - 1)
    if (j != n-1):
        if (bricks[i][j + 1] == 1 and stability[i][j + 1] != 1):
            stability[i][j + 1] = 1
            detect_stability(i, j + 1)
for j in range(n):
    if(bricks[0][j]==1):
        detect_stability(0,j)
stable_bricks=0
for i in stability:
    stable_bricks+=sum(i)
result=[]
for k in operations:
    i,j=map(int,k)
    bricks[i][j]=0
    stability=copy.deepcopy(record_topBricks)
    for l in range(n):
        if (bricks[0][l] == 1):
            detect_stability(0, l)
    temp=0
    for l in stability:
        temp += sum(l)
    result.append(stable_bricks-temp-1)
    stable_bricks=temp
print(result)