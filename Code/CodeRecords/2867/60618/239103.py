line=[[0]*5]*5
for i in range(0,5):
    line[i]=list(input().split())
for i in range(0,5):
    for j in range(0,5):
        if line[i][j]==1:
            step=abs(i-2)+abs(j-2)
            print(step)