source = input().replace('[','').replace(']','').split(',')
moves = []
for a in range(0,len(source)//2):
    move=[int(source[2*a]),int(source[2*a+1])]
    moves.append(move)
map=[]
for a in range(0,3):
    map.append(['-','-','-'])
for i in range(0,len(moves)):
    if i%2==0:
        map[moves[i][0]][moves[i][1]]='A'
    elif i%2==1:
        map[moves[i][0]][moves[i][1]]='B'
#check
result = ""
flag = False
for row in range(0,3):
    if map[row][0]==map[row][1]==map[row][2]!='-':
        result = map[row][0]
        flag = True
        break
if not flag:
    for column in range(0,3):
        if map[0][column]==map[1][column]==map[2][column]!='-':
            result = map[0][column]
            flag = True
            break
if not flag:
    for diagonal in range(0,1):
        if map[0][0]==map[1][1]==map[2][2]:
            result = map[0][0]
            flag = True
            break
        if map[0][2] == map[1][1] == map[2][0]:
            result = map[2][0]
            flag = True
            break
if flag:
    print(result)
else:
    for i in range(0,3):
        for j in range(0,3):
            if map[i][j]=='-':
                flag=True
                break
        if flag:
            break
    if flag:
        print("Pending")
    else:
        print("Draw")
