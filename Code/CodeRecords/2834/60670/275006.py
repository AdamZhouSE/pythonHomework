def tryans(s,depth):
    if depth==0:
        global maxscore
        tmpscore=0
        for i in range(0,n):
            for j in range(0,m):
                if s[j]==stu[i][j]:
                    tmpscore+=score[j]
        if tmpscore>maxscore:
            maxscore=tmpscore
        return
    tryans(s+'A',depth-1);
    tryans(s+'B',depth-1);
    tryans(s+'C',depth-1);
    tryans(s+'D',depth-1);
    tryans(s+'E',depth-1);

n,m=map(int,input().split())
maxscore=0
stu=[]
for i in range(0,n):
    stu.append(input())
score=list(map(int,input().split()))
tryans("",m)
print(maxscore)