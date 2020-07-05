str = int(input())

lst = []
while str >= 1:
    forehead = int(str/26)
    if str==26:
        forehead = 0
        left = 26
    else:
        left = str - forehead*26
    if left == 1:
        lst.insert(0,'A')
    elif left == 2:
        lst.insert(0,'B')
    elif left == 3:
        lst.insert(0,'C')
    elif left == 4:
        lst.insert(0,'D')
    elif left == 5:
        lst.insert(0,'E')
    elif left == 6:
        lst.insert(0,'F')
    elif left == 7:
        lst.insert(0,'G')
    elif left == 8:
        lst.insert(0,'H')
    elif left == 9:
        lst.insert(0,'I')
    elif left == 10:
        lst.insert(0,'J')
    elif left == 11:
        lst.insert(0,'K')
    elif left == 12:
        lst.insert(0,'L')
    elif left == 13:
        lst.insert(0,'M')
    elif left == 14:
        lst.insert(0,'N')
    elif left == 15:
        lst.insert(0,'O')
    elif left == 16:
        lst.insert(0,'P')
    elif left == 17:
        lst.insert(0,'Q')
    elif left == 18:
        lst.insert(0,'R')
    elif left == 19:
        lst.insert(0,'S')
    elif left == 20:
        lst.insert(0,'T')
    elif left == 21:
        lst.insert(0,'U')
    elif left == 22:
        lst.insert(0,'V')
    elif left == 23:
        lst.insert(0,'W')
    elif left == 24:
        lst.insert(0,'X')
    elif left == 25:
        lst.insert(0,'Y')
    elif left == 26 or left ==0:
        lst.insert(0,'Z')
    else:
        break
    str = forehead
    print("".join(lst))