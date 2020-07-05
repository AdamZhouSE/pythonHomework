def check(ball):
    #斜向赢1
        if ball[0][0]==ball[1][1]==ball[2][2]=='A':
            return 'A'
        if ball[0][0]==ball[1][1]==ball[2][2]=='B':
            return 'B'
    #斜向赢2
        if ball[0][2]==ball[1][1]==ball[2][0]=='A':
            return 'A'
        if ball[0][2]==ball[1][1]==ball[2][0]=='B':
            return 'B'
    #横向赢
        for i in range(0,2):
            if ball[i][2]==ball[i][1]==ball[i][0]=='A':
                return 'A'
            if ball[i][2]==ball[i][1]==ball[i][0]=='B':
                return 'B'
    #纵向赢
        for i in range(0,2):
            if ball[0][i]==ball[1][i]==ball[2][i]=='A':
                return 'A'
            if ball[0][i]==ball[1][i]==ball[2][i]=='B':
                return 'B'
    #平局
        if not ('X' in ball[0]and 'X' in ball[1] and 'X' in ball[2]):
            return "Draw"
        else:
            return"Pending"

#处理输入
Str=input()
Str=Str.replace("[",'')
Str=Str.replace("]",'')
Str=Str.replace(",",'')
ball=[['X','X','X'],['X','X','X'],['X','X','X']]
#放置
l=int(len(Str)/2)
for i in range(0,l):
    x=int(Str[0])
    y=int(Str[1])
    Str=Str[2:]
    if i%2==0:
        ball[x][y]='A'
    else:
        ball[x][y]='B'
result=check(ball)
print(result)