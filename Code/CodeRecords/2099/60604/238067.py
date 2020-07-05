def conv(a):
    if a=="A":
        return 1
    elif a=="B":
        return 2
    elif a=="C":
        return 3
    elif a=="D":
        return 4
    elif a=="E":
        return 5
    elif a=="F":
        return 6
    elif a=="G":
        return 7
    elif a=="H":
        return 8
    elif a=="I":
        return 9
    elif a=="J":
        return 10
    elif a=="K":
        return 11
    elif a=="L":
        return 12
    elif a=="M":
        return 13
    elif a=="N":
        return 14
    elif a=="O":
        return 15
    elif a=="P":
        return 16
    elif a=="Q":
        return 17
    elif a=="R":
        return 18
    elif a=="S":
        return 19
    elif a=="T":
        return 20
    elif a=="U":
        return 21
    elif a=="V":
        return 22
    elif a=="W":
        return 23
    elif a=="X":
        return 24
    elif a=="Y":
        return 25
    else:
        return 26
    
    
n=input()
if len(n) ==1:
    print(conv(n))
else:
    print(26*conv(n[0])+conv(n[1]))