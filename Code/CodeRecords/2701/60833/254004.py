list1 = list(str(input())[2:-2].split("],["))
n = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a = 1
panding=""

def judge(n):
    if n[0][0]==n[0][1]==n[0][2]:
        if n[0][0] == 1:
            return "Awin"
        elif n[0][0] == 2:
            return "Bwin"
        else:
            return "todo"
    elif n[1][0]==n[1][1]==n[1][2]:
        if n[1][0] == 1:
            return "Awin"
        elif n[1][0] == 2:
            return "Bwin"
        else:
            return "todo"
    elif n[2][0]==n[2][1]==n[2][2]:
        if n[2][0] == 1:
            return "Awin"
        elif n[2][0] == 2:
            return "Bwin"
        else:
            return "todo"
    elif n[0][0]==n[1][0]==n[2][0]:
        if n[0][0] == 1:
            return "Awin"
        elif n[0][0] == 2:
            return "Bwin"
        else:
            return "todo"
    elif n[0][1]==n[1][1]==n[2][1]:
        if n[0][1] == 1:
            return "Awin"
        elif n[0][1] == 2:
            return "Bwin"
        else:
            return "todo"
    elif n[0][2]==n[1][2]==n[2][2]:
        if n[0][2] == 1:
            return "Awin"
        elif n[0][2] == 2:
            return "Bwin"
        else:
            return "todo"
    elif n[0][0] == n[1][1] == n[2][2]:
        if n[0][0] == 1:
            return "Awin"
        elif n[0][0] == 2:
            return "Bwin"
        else:
            return "todo"
    elif n[0][2] == n[1][1] == n[2][0]:
        if n[0][2] == 1:
            return "Awin"
        elif n[0][2] == 2:
            return "Bwin"
        else:
            return "todo"
    else:return "todo"
    pass


for i in list1:
    p = int(i[0:1])
    q = int(i[-1])
    if a % 2:
        n[p][q] = 1
    else:
        n[p][q] = 2
    a=a+1
    panding=judge(n)
    if panding=="Awin":
        print("A")
        break
    elif panding=="Bwin":
        print("B")
        break
if panding=="todo":
    x=0
    t = 0
    for i in n:
        for j in i:
            if j == 0:
                print("Pending")
                t = 1
                break
            x = x + 1
        if t == 1:
            break
    if x == 9:
        print("Draw")