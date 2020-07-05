list1=input().split(',')
cnt_X=0
cnt_O=0
for i in range(0,3):
    for j in range(0,3):
        if list1[i][j]=='X':
            cnt_X+=1
        elif list1[i][j]=='O':
            cnt_O+=1
if cnt_O>cnt_X or cnt_X-cnt_O>=2:
    print(False)
else:
    xwin = False
    if list1[0][0] == 'X' and list1[0][1] == 'X' and list1[0][2] == 'X' or list1[1][0] == 'X' and list1[1][1] == 'X' and \
            list1[1][2] == 'X' or list1[2][0] == 'X' and list1[2][1] == 'X' and list1[2][2] == 'X' or list1[0][
        0] == 'X' and list1[1][0] == 'X' and list1[2][0] == 'X' or list1[0][1] == 'X' and list1[1][1] == 'X' and \
            list1[2][1] == 'X' or list1[0][2] == 'X' and list1[1][2] == 'X' and list1[2][2] == 'X' or list1[0][
        0] == 'X' and list1[0][1] == 'X' and list1[0][2] == 'X' or list1[1][0] == 'X' and list1[1][1] == 'X' and \
            list1[1][2] == 'X' or list1[0][0] == 'X' and list1[1][1] == 'X' and list1[2][2] == 'X' or list1[0][
        0] == 'X' and list1[0][1] == 'X' and list1[0][2] == 'X' or list1[1][0] == 'X' and list1[1][1] == 'X' and \
            list1[1][2] == 'X' or list1[0][2] == 'X' and list1[1][1] == 'X' and list1[2][0] == 'X':
        xwin = True
    owin = False
    if list1[0][0] == 'O' and list1[0][1] == 'O' and list1[0][2] == 'O' or list1[1][0] == 'O' and list1[1][1] == 'O' and \
            list1[1][2] == 'O' or list1[2][0] == 'O' and list1[2][1] == 'O' and list1[2][2] == 'O' or list1[0][
        0] == 'O' and list1[1][0] == 'O' and list1[2][0] == 'O' or list1[0][1] == 'O' and list1[1][1] == 'O' and \
            list1[2][1] == 'O' or list1[0][2] == 'O' and list1[1][2] == 'O' and list1[2][2] == 'O' or list1[0][
        0] == 'O' and list1[0][1] == 'O' and list1[0][2] == 'O' or list1[1][0] == 'O' and list1[1][1] == 'O' and \
            list1[1][2] == 'O' or list1[0][0] == 'O' and list1[1][1] == 'O' and list1[2][2] == 'O' or list1[0][
        0] == 'O' and list1[0][1] == 'O' and list1[0][2] == 'O' or list1[1][0] == 'O' and list1[1][1] == 'O' and \
            list1[1][2] == 'O' or list1[0][2] == 'O' and list1[1][1] == 'O' and list1[2][0] == 'O':
        owin = True
    if cnt_X==cnt_O:
        if xwin==True:
            print(False)
        else:
            print(True)
    elif cnt_X-cnt_O==1:
        if owin:
            print(False)
        else:
            print(True)