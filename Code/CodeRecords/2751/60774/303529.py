import sys

def isClear(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if(matrix[i][j] == -1):
                return False
    return True

def findWay(matrix,pos):
    around = []
    if(pos[0] == 0):
        if(pos[1] == 0):
            around = [matrix[pos[0] + 1][pos[1]],matrix[pos[0]][pos[1] + 1]]
        elif(pos[1] == len(matrix[0]) - 1):
            around = [matrix[pos[0] + 1][pos[1]],matrix[pos[0]][pos[1] - 1]]
        else:
            around = [matrix[pos[0] + 1][pos[1]],matrix[pos[0]][pos[1] - 1],matrix[pos[0]][pos[1] + 1]]
    elif(pos[0] == len(matrix) - 1):
        if(pos[1] == 0):
            around = [matrix[pos[0] - 1][pos[1]],matrix[pos[0]][pos[1] + 1]]
        elif(pos[1] == len(matrix[0]) - 1):
            around = [matrix[pos[0] - 1][pos[1]],matrix[pos[0]][pos[1] - 1]]
        else:
            around = [matrix[pos[0] - 1][pos[1]],matrix[pos[0]][pos[1] - 1],matrix[pos[0]][pos[1] + 1]]
    elif(pos[1] == 0):
        around = [matrix[pos[0]][pos[1] + 1],matrix[pos[0] + 1][pos[1]],matrix[pos[0] - 1][pos[1]]]
    elif(pos[1] == len(matrix[0]) - 1):
        around = [matrix[pos[0]][pos[1] - 1],matrix[pos[0] + 1][pos[1]],matrix[pos[0] - 1][pos[1]]]
    else:
        around = [matrix[pos[0]][pos[1] + 1],matrix[pos[0]][pos[1] - 1],matrix[pos[0] + 1][pos[1]],matrix[pos[0] - 1][pos[1]]]
    return around
    
matrix = []
while(True):
    line = sys.stdin.readline().strip()
    if line == '':
        break
    matrix.append(list(map(int,line.split())))
distance = []
for i in range(0,len(matrix)):
    distance.append([-1 for i in range(0,len(matrix[0]))])
for k in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        if(matrix[k][j] == 0):
            distance[k][j] = 0 
while(not isClear(distance)):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if(distance[i][j] == -1):
                around = findWay(distance,[i,j])
                around = list(filter(lambda x: x != -1,around))
                if(around != []):
                    distance[i][j] = min(around) + 1
for w in distance:
    res = ' '.join(list(map(str,w)))
    print(res)