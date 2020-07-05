def judge(string,player):
    string=string.split(',')
    for i in range(3):
        if string[i]==player*3:
            return True
        elif string[0][i]==string[1][i] and string[1][i]==string[2][i] and string[0][i]==player:
            return True
    if string[0][0]==string[1][1] and string[1][1]==string[2][2] and string[0][0]==player:
        return True
    elif string[0][2]==string[1][1] and string[1][1]==string[2][0] and string[1][1]==player:
        return True
    return False
temp=input()
flag=True
if temp.count('X')<temp.count('O') or temp.count('X')>temp.count('O')+1:
    flag=False
else:
    if temp.count('X')==temp.count('O'):
        if judge(temp,'X'):
            flag=False
    else:
        if judge(temp,'O'):
            flag=False
print(flag)