stones=eval(input())
i=0
move=0
for i in range(0,len(stones)):
    if(stones[i][0]==-1):
        continue
    else:
        tmp=[stones[i][0],stones[i][1]];
    for j in range(i,len(stones)):
        if(stones[j][0]==tmp[0] or stones[j][1]==tmp[1]):
            move+=1;
            stones[j][0]=-1;
            stones[j][1]=-1;
            
print(move)