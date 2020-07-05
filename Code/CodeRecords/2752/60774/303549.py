def isClear(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if(matrix[i][j] > 1):
                return False
    return True

def findWay(matrix,pos):
    nextStep = []
    if(pos[0] == 0):
        if(pos[1] == 0):
            if(matrix[pos[0] + 1][pos[1]] >= 1):
                nextStep = [pos[0] + 1,pos[1]]
            elif(matrix[pos[0]][pos[1] + 1] >= 1):
                nextStep = [pos[0],pos[1] + 1]
        elif(pos[1] == len(matrix[0]) - 1):
            if(matrix[pos[0] + 1][pos[1]] >= 1):
                nextStep = [pos[0] + 1,pos[1]]
            elif(matrix[pos[0]][pos[1] - 1] >= 1):
                nextStep = [pos[0],pos[1] - 1]
        else:
            if(matrix[pos[0] + 1][pos[1]] >= 1):
                nextStep = [pos[0] + 1,pos[1]]
            elif(matrix[pos[0]][pos[1] - 1] >= 1):
                nextStep = [pos[0],pos[1] - 1]
            elif(matrix[pos[0]][pos[1] + 1] >= 1):
                nextStep = [pos[0],pos[1] + 1]
    elif(pos[0] == len(matrix) - 1):
        if(pos[1] == 0):
            if(matrix[pos[0] - 1][pos[1]] >= 1):
                nextStep = [pos[0] - 1,pos[1]]
            elif(matrix[pos[0]][pos[1] + 1] >= 1):
                nextStep = [pos[0],pos[1] + 1]
        elif(pos[1] == len(matrix[0]) - 1):
            if(matrix[pos[0] - 1][pos[1]] >= 1):
                nextStep = [pos[0] - 1,pos[1]]
            elif(matrix[pos[0]][pos[1] - 1] >= 1):
                nextStep = [pos[0],pos[1] - 1]
        else:
            if(matrix[pos[0] - 1][pos[1]] >= 1):
                nextStep = [pos[0] - 1,pos[1]]
            elif(matrix[pos[0]][pos[1] - 1] >= 1):
                nextStep = [pos[0],pos[1] - 1]
            elif(matrix[pos[0]][pos[1] + 1] >= 1):
                nextStep = [pos[0],pos[1] + 1]
    elif(pos[1] == 0):
        if(matrix[pos[0]][pos[1] + 1] >= 1):
            nextStep = [pos[0],pos[1] + 1]
        elif(matrix[pos[0] + 1][pos[1]] >= 1):
            nextStep = [pos[0] + 1,pos[1]]
        elif(matrix[pos[0] - 1][pos[1]] >= 1):
            nextStep = [pos[0] - 1,pos[1]]
    elif(pos[1] == len(matrix[0]) - 1):
        if(matrix[pos[0]][pos[1] - 1] >= 1):
            nextStep = [pos[0],pos[1] - 1]
        elif(matrix[pos[0] + 1][pos[1]] >= 1):
            nextStep = [pos[0] + 1,pos[1]]
        elif(matrix[pos[0] - 1][pos[1]] >= 1):
            nextStep = [pos[0] - 1,pos[1]]
    else:
        if(matrix[pos[0]][pos[1] + 1] >= 1):
            nextStep = [pos[0],pos[1] + 1]
        elif(matrix[pos[0]][pos[1] - 1] >= 1):
            nextStep = [pos[0],pos[1] - 1]
        elif(matrix[pos[0] + 1][pos[1]] >= 1):
            nextStep = [pos[0] + 1,pos[1]]
        elif(matrix[pos[0] - 1][pos[1]] >= 1):
            nextStep = [pos[0] - 1,pos[1]]
    return nextStep
    
forest = []
while(True):
    s = input().strip().strip(',')
    if(s == ']'):
        break
    if(s != '['):
        forest.append(eval(s))
start = [0,0]
forest[0][0] = 0
steps = 0
while(not isClear(forest)):
    next = findWay(forest,start)
    if(next == []):
        break
    else:
        forest[next[0]][next[1]] = 0
        start = next
        steps = steps + 1
if(isClear(forest)):
    print(steps)
else:
    print(-1)