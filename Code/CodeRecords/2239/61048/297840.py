def numop27():
    str_in=input()
    board=str_in.split(',')
    x=0
    o=0
    set=[]
    res=True
    for char in str_in:
        if(char=='X'):
            x+=1
        if(char=='O'):
            o+=1
    for i in range(3):
        set.append([x for x in board[i]])
    x_first=(x-1==o) or (x==o)
    x_win=win(set,'X')
    o_win=win(set,'O')
    if(x_win and o_win):
        res=False
    if(not x_first):
        res=False
    print(res)
    return 0

def win(set,c):
    res=False
    for i in range(3):
        if set[i][0]==c and set[i][1]==c and set[i][2]==c:
            res=True
        if set[0][i]==c and set[1][i]==c and set[2][i]==c:
            res=True
        if set[0][0]==c and set[1][1]==c and set[2][2]==c:
            res=True
        if set[2][0]==c and set[1][1]==c and set[0][2]==c:
            res=True
    return res


numop27()