times=int(input());
pokers=input().split(" ");###点数记住是字符串！！
flag=1;
player1=0;
player2=0;
lo=0;
hi=times-1;
tepnumblo=0;
tepnumbhi=0;
number=0;
while lo!=hi:
    tepnumblo=int(pokers[lo]);
    tepnumbhi=int(pokers[hi]);
    if tepnumblo >= tepnumbhi:
        number=tepnumblo;
        lo=lo+1;
    else:
        number = tepnumbhi;
        hi = hi - 1;
    if flag==1:
        player1=player1+number;
        flag=-flag;
    else:
        player2=player2+number
        flag=-flag;
number=int(pokers[lo]);
if flag==1:
    player1=player1+number;
    flag=-flag;
else:
    player2=player2+number
    flag=-flag;
result=str(player1)+" "+str(player2);
print(result)