def checkWin(checker):
    #下面检查横排有没有连在一起：
    hasWiner = 0
    for i in range(0,3):
        if checker[i][0]==checker[i][1] and checker[i][0]==checker[i][2] and checker[i][1]==checker[i][2] and checker[i][0]!=None:
            hasWiner=1
            break
    if hasWiner==1:
        return True
    #下面检查竖排有没有连在一起：
    hasWiner = 0
    for i in range(0, 3):
       if checker[0][i]==checker[1][i] and checker[1][i]==checker[2][i] and checker[0][i]==checker[2][i] and checker[0][i]!=None:
           hasWiner=1
           break
    if hasWiner==1:
        return True
    #下面检查左对角线有没有连在一起：
    hasWiner = 1
    i=0
    j=0
    while i<2 and j<2:
        if checker[i][j]!=checker[i+1][j+1] or checker[i][j]==None:
            hasWiner=0
            break
        i=i+1
        j=j+1
    if hasWiner==1:
        return True
    #下面检查右对角线有没有连在一起
    hasWiner=1
    i=0
    j=2
    while i<2 and j>0:
        if checker[i][j]!=checker[i+1][j-1] or checker[i][j]==None:
            hasWiner=0
            break
        i=i+1
        j=j-1
    if hasWiner==1:
        return True
    return False

def checkerIsFull(check):
    n=0
    for i in range(3):
        for j in range(3):
            if checker[i][j]!=None:
                n=n+1
    if n==9:
        return True
    return False

winer="Draw"
s=input()
s=","+s[1:len(s)-1]

ls=s.split("]")#步骤数组
del ls[len(ls)-1]
for i in range(len(ls)):
    ls[i]=(ls[i])[2:]
#print(ls)

checker=[None]*3#棋盘数组
for i in range(3):
    checker[i]=[None]*3

for i in range(len(ls)):
    if checkerIsFull(checker):
        winer="Pending"
        break
    if i%2==0:#A动
        hang=int(ls[i][:ls[i].index(",")])
        lie=int(ls[i][ls[i].index(",")+1:])
        if checker[hang][lie]==None:
            checker[hang][lie]='X'
        else:
            continue
        if checkWin(checker):
            winer="A"
            break
    if i%2==1:#B动
        hang=int(ls[i][:ls[i].index(",")])
        lie=int(ls[i][ls[i].index(",")+1:])
        if checker[hang][lie]==None:
            checker[hang][lie]='O'
        else:
            continue
        if checkWin(checker):
            winer="B"
            break
        
    #print(checker)

if len(ls)>9 or (winer=="Draw" and len(ls)<9):
    #"Pending"的情况：1.len(ls)>9（之后的步骤没有格子可填），无论之前有没有决出胜者  2.len(ls)<9而且之前没有决出胜者
    winer="Pending"
print(winer)



