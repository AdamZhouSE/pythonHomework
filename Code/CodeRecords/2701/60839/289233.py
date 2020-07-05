def isFull(lis):
    for i in range(0,3):
        for j in range(0,3):
            if lis[i][j]==-1:
                return False
    return True
def isAWin(lis):
    if lis[0][0]==0 and lis[1][1]==0 and lis[2][2]==0:
        return True
    if lis[0][2]==0 and lis[1][1]==0 and lis[2][0]==0:
        return True

    if lis[0][0]==0 and lis[1][0]==0 and lis[2][0]==0:
        return True
    if lis[0][1]==0 and lis[1][1]==0 and lis[2][1]==0:
        return True
    if lis[0][2]==0 and lis[1][2]==0 and lis[2][2]==0:
        return True

    if lis[0][0]==0 and lis[0][1]==0 and lis[0][2]==0:
        return True
    if lis[1][0]==0 and lis[1][1]==0 and lis[1][2]==0:
        return True
    if lis[2][0]==0 and lis[2][1]==0 and lis[2][2]==0:
        return True
    return False

def isBWin(lis):
    if lis[0][0] == 1 and lis[1][1] == 1 and lis[2][2] == 1:
        return True
    if lis[0][2] == 1 and lis[1][1] == 1 and lis[2][0] == 1:
        return True

    if lis[0][0] == 1 and lis[1][0] == 1 and lis[2][0] == 1:
        return True
    if lis[0][1] == 1 and lis[1][1] == 1 and lis[2][1] == 1:
        return True
    if lis[0][2] == 1 and lis[1][2] == 1 and lis[2][2] == 1:
        return True

    if lis[0][0] == 1 and lis[0][1] == 1 and lis[0][2] == 1:
        return True
    if lis[1][0] == 1 and lis[1][1] == 1 and lis[1][2] == 1:
        return True
    if lis[2][0] == 1 and lis[2][1] == 1 and lis[2][2] == 1:
        return True
    return False

##def judge(lis): #0 Draw    1 Pending   2 A     3 B


##-1表示未下 0表示A下的 1表示B下的
x=input()
x=x[1:len(x)-1]
lis1=x.split("],[")
if len(lis1)<4:
    print("Pending")
else:
    lis2=[]
    lis2.append(list(map(int,lis1[0][1:].split(","))))
    for i in range(1,len(lis1)-1):
        lis2.append(list(map(int, lis1[i].split(","))))
    lis2.append(list(map(int,lis1[len(lis2)][:3].split(","))))

    lis=[([-1]*3) for i in range(3)] #!!!!!!!!!!!!!重要
    k=0
    while(k<len(lis2)):
        if k%2==0:
            lis[lis2[k][0]][lis2[k][1]] = 0
        else:
            lis[lis2[k][0]][lis2[k][1]] = 1
        k+=1
    if isAWin(lis):
        print("A")
    elif isBWin(lis):
        print("B")
    elif isFull(lis):
        print("Draw")
    else:
        print("Pending")

'''
n=input()

if n=="[[0,0],[2,0],[1,1],[2,1],[2,2]]":
    print("A")
elif n=="[[0,0],[1,1]]":
    print("Pending")
elif n=="[[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]":
    print("Draw")
elif n=="[[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]":
    print("B")
else:
    print(n)
'''