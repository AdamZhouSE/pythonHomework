input()
M = []
string = input()
while string != "]":
    M.append([int(x[1:-1:1]) for x in string[3:string.index("]"):1].split(",")])
    string = input()
newM = []
for x in range(len(M)):
    line = []
    for y in range(len(M[0])):
        count = 0
        while y + count < len(M[0]) and M[x][y + count] == 1:
            count += 1
        line.append(count)
    newM.append(line)
maxS = 0
for x in range(len(M)):
    for y in range(len(M[0])):
        littleM = []
        for newx in range(x, len(M)):
            littleM.append(newM[newx][y])
        for newx in range(len(littleM)):
            S = min(littleM[:len(littleM) - newx:]) * newx
            if S > maxS:
                maxS = S
print(maxS)
