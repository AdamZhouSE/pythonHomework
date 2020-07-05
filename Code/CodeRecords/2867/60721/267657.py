import math
lis=[list()]*5
for i in range(0,5):
    lis[i]=list(map(int,input().split(" ")))
p=[0,0]
for i in range(0,5):
    for j in range(0,5):
        if(lis[i][j]==1):
            p=[i,j]
print(int(math.fabs(p[0]-2))+int(math.fabs(p[1]-2)))