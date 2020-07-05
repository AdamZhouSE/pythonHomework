import math

class Direction():
    def __init__(self,cur,left = None,right = None):
        self.cur = cur
        self.left = left
        self.right = right
   
    def getCur(self):
        return self.cur
    
    def setLeft(self,left):
        self.left = left
    
    def setRight(self,right):
        self.right = right
    
    def turnLeft(self):
        return self.left
    
    def turnRight(self):
        return self.right
    
    def turnAround(self):
        return self.turnRight().turnRight()

def move(curDir,curPos,distance):
    if(curDir.getCur() == 'E'):
        curPos[0] = curPos[0] + distance
    elif(curDir.getCur() == 'W'):
        curPos[0] = curPos[0] - distance
    elif(curDir.getCur() == 'N'):
        curPos[1] = curPos[1] + distance
    elif(curDir.getCur() == 'S'):
        curPos[1] = curPos[1] - distance
    return curPos

if __name__ == '__main__':
    East = Direction('E')
    West = Direction('W')
    North = Direction('N',West,East)
    South = Direction('S',East,West)
    East.setLeft(North)
    East.setRight(South)
    West.setLeft(South)
    West.setRight(North)
    t = int(input())
    for i in range(0,t):
        numOfStep = int(input())
        step = input().split(' ')
        curDir = North
        curPos = [0,0]
        for j in range(0,2 * numOfStep,2):
            if(step[j] == 'R'):
                curDir = curDir.turnRight()
            elif(step[j] == 'L'):
                curDir = curDir.turnLeft()
            elif(step[j] == 'D'):
                curDir = curDir.turnAround()
            '''print(curDir.getCur())'''
            curPos = move(curDir,curPos,int(step[j + 1]))
            '''print(curPos)'''
        distance = int(math.sqrt(curPos[0] *curPos[0] + curPos[1] * curPos[1]))
        direction = curDir.getCur()
        print(str(distance) + ' ' + direction)