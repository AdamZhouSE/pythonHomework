def main():
    a = "".join(input().split("["))
    a = "".join(a.split("]"))
    a = list(map(int,a.split(",")))
    b = [[0 for i in range(3)]for j in range(3)]
    moveA = True
    result = "Pending"
    for i in range(0,len(a)-1,2):
        if moveA:
            b[a[i]][a[i+1]] = 1
            moveA = False
        else:
            b[a[i]][a[i + 1]] = -1
            moveA = True
    if row(b) == "Pending" and column(b) == "Pending" and diagonal(b) == "Pending":
        if draw(b)=="Draw": print("Draw")
        else:print("Pending")
    else :
        if row(b) == "A" or column(b) == "A" or diagonal(b) == "A":print("A")
        else:print("B")


def row(b):
    str = "Pending"
    for i in range(3):
        if b[i][0] == b[i][1] and b[i][1] == b[i][2]:
            if b[i][0] == 1: str = "A"
            elif b[i][0]==-1: str = "B"
            break
    return str

def column(b):
    str = "Pending"
    for i in range(3):
        if b[0][i] == b[1][i] and b[1][i] == b[2][i]:
            if b[0][i] == 1:
                str = "A"
            elif b[0][i]==-1:
                str = "B"
            break
    return str

def diagonal(b):
    str = "Pending"
    if b[0][0] == b[1][1] and b[1][1]==b[2][2]:
        if b[0][0] == 1: str = "A"
        elif b[0][0]==-1 : str = "B"
    elif b[2][0] == b[1][1] and b[1][1] == b[0][2]:
        if b[1][1] == 1:str = "A"
        elif b[1][1]==-1:str = "B"
    return str

def draw(b):
    str = "Draw"
    for i in range(3):
        for j in range(3):
            if b[i][j]==0:
                str = "Pending"
                break
    return str



if __name__ == '__main__':
    main()
