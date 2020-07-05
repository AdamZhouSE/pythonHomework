def stringToArray(string):
    string=string[2:len(string)-2]
    temp=string.split("],[")
    length=len(temp)
    array=[[0]*2]*length
    for i in range (0,length):
        array[i]=temp[i].split(',')
    return array
def move(player,row,line,array):
    array[int(row)][int(line)]=player
    return array
def check(array):
    for i in range(3):
        if array[i][0]==array[i][1] and array[i][0]==array[i][2] and array[i][0]!=0:
            return True
        elif array[0][i]==array[1][i] and array[0][i]==array[2][i] and array[0][i]!=0:
            return True
    if array[0][0]==array[1][1] and array[0][0]==array[2][2] and array[0][0]!=0:
        return True
    elif array[0][2]==array[1][1] and array[0][2]==array[2][0] and array[0][2]!=0:
        return True
    else:
        return False
array=stringToArray(input())
table=[[0 for _ in range(3)] for _ in range(3)]
for i in range(len(array)):
    if i % 2==0:
        table=move("A",array[i][0],array[i][1],table)
        flag=check(table)
        if flag :
            print("A")
            break
    else:
        table=move("B",array[i][0],array[i][1],table)
        flag=check(table)
        if flag :
            print("B")
            break
if not flag:
    if len(array)==9:
        print("Draw")
    else:
        print("Pending")