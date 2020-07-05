#格式化输入
def setChess(table,pos_str,label):
    x = int(pos_str[1])
    y = int(pos_str[3])
    table[x][y] = label

def isWin(table,pos_str):
    x = int(pos_str[1])
    y = int(pos_str[3])
    if table[x][0] == table[x][1] and table[x][1] == table[x][2] and table[x][0] != -1:
        return True
    elif table[0][y] == table[1][y] and table[1][y] == table[2][y] and table[0][y] != -1:
        return True
    elif table[0][0] == table[1][1] and table[1][1] == table[2][2] and table[0][0] != -1:
        return True
    elif table[0][2] == table[1][1] and table[1][1] == table[2][0] and table[0][2] != -1:
        return True

line = input()
sentinel = 0#表示是否对局结束
pos = line[1:len(line)-1].split("],")
table = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
for i in range(0,len(pos)):
    setChess(table,pos[i],i%2)
    if(isWin(table,pos[i])):
        if(i%2 != 1):
            print("A")
            sentinel = 1
            break
        else:
            print("B")
            sentinel = 1
            break
if(len(pos) == 9 and sentinel == 0):
    print("Draw")
elif sentinel == 0:
    print("Pending")

