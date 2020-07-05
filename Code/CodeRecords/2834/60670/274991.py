def tryans(s,depth,m):
    if m==0:
        for i in range(0,n):
            tmpscore=0
            for j in range(0,m):
                if s[j]==stu[i][j]:
                    tmpscore+=score[j]
            if tmpscore>maxscore:
                maxscore=tmpscore
        return
    tryans(s+'A',depth-1,m);
    tryans(s+'B',depth-1,m);
    tryans(s+'C',depth-1,m);
    tryans(s+'D',depth-1,m);
    tryans(s+'E',depth-1,m);

n,m=map(int,input().split())
stu=[]
for i in range(0,n):
    stu.append(input())
score=list(map(int,input().split()))
maxscore=0