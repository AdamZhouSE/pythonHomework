s = input()
Lnum = 0
Rnum = 0
NWSE = [True]
point = [0,0]
for i in range(3):
    NWSE.append(False)
for i in range(len(s)):
    if(s[i] == 'L'):
        Lnum += 1
        for x in range(4):
            if(NWSE[x] == True):
                NWSE[x] = False
                NWSE[(x+1)%4] = True
    elif(s[i] == 'R'):
        Rnum += 1 
        for x in range(4):
            if(NWSE[x] == True):
                NWSE[x] = False
                NWSE[(x-1)%4] = True
    else:
        if(NWSE[0]):
            point[1] += 1
        elif(NWSE[1]):
            point[0] -= 1
        elif(NWSE[2]):
            point[1] -= 1
        elif(NWSE[3]):
            point[0] += 1
if((Lnum-Rnum)%4==0):
    if(point == [0,0]):
        print(True)
    else:
        print(False)
else:
    print(True)