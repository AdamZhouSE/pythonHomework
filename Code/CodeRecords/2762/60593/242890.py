t=int(input())
D=['N','E','S','W']
for tt in range(t):
    n=int(input())
    direction=0
    move=list(input().split())
    loc=[0]*4
    for i in range(0,2*n,2):
        if(move[i]=='U'):
            pass
        elif(move[i]=='R'):
            direction=(direction+1)%4
        elif(move[i]=='L'):
            tmp=direction-1
            direction=tmp if tmp>=0 else 3
        else:
            direction=(direction+2)%4
        loc[direction]+=int(move[i+1])
    x=loc[1]-loc[3]
    y=loc[0]-loc[2]
    print(int((x**2+y**2)**0.5),D[direction])
