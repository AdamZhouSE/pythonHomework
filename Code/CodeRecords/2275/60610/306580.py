num=int(input());
board=[];
for i in range(num):
    row=list(map(int,input().split(",")));
    board.append(row);
count=0
for i in range(num):
    for j in range(num):
        if(board[0][0]^board[0][j]^board[i][0]^board[i][j]==1):
            count=1;
if(count==1):
    print(-1);
else:
    row=0;
    col=0;
    cntrow=0;
    cntcol=0;
    for i in range(num):
        row+=board[0][i];
        col+=board[i][0];
        if(board[0][i]!=i%2):
            cntrow+=1;
        if(board[i][0]!=i%2):
            cntcol+=1;
    if(row<num//2)|(row>(num+1)//2):
        count=1;
    if (col < num // 2) | (col > (num + 1) // 2):
        count = 1;
    res=0;
    if(num%2==0):
        res+=min(cntrow,num-cntrow);
        res+=min(cntcol,num-cntcol);
    else:
        if(cntrow%2==1):
            cntrow=num-cntrow;
        if(cntcol%2==1):
            cntcol=num-cntcol;
        res=cntrow+cntcol;
    if(count==1):
        print(-1);
    else:
        print(res//2)