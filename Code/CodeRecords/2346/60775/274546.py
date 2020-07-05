def print_matrix(mat:list):
    for i in range(len(mat)):
        print(mat[i])

class Matirx:
    def __init__(self,matrix:list):
        self.matrix = matrix
        self.pos = [1,1]
        self.direction = ['right','down','left','up']
        self.nowDir = 0


    def chageDir(self):
        if self.nowDir == 3:
            self.nowDir = 0
        else:
            self.nowDir += 1
        return self.direction[self.nowDir]

    def currentDir(self):
        return self.direction[self.nowDir]

    def oneStep(self):
        current_pos = [self.pos[0],self.pos[1]]
        now = self.matrix[self.pos[0]][self.pos[1]]
        up = self.matrix[self.pos[0]-1][self.pos[1]]
        down = self.matrix[self.pos[0]+1][self.pos[1]]
        left = self.matrix[self.pos[0]][self.pos[1]-1]
        right = self.matrix[self.pos[0]][self.pos[1]+1]
        if up == None and down == None and left == None and right == None:
            return now
        if self.currentDir() == 'right':
            if right == None:
                self.chageDir()
                self.pos[0] += 1
            else:
                self.pos[1] += 1
        elif self.currentDir() == 'down':
            if down == None:
                self.chageDir()
                self.pos[1] -= 1
            else:
                self.pos[0] += 1
        elif self.currentDir() == 'left':
            if left == None:
                self.chageDir()
                self.pos[0] -= 1
            else:
                self.pos[1] -= 1
        elif self.currentDir() == 'up':
            if up == None:
                self.chageDir()
                self.pos[1] += 1
            else:
                self.pos[0] -= 1
        self.matrix[current_pos[0]][current_pos[1]] = None
        return now

    def go(self):
        result = []
        num = (len(self.matrix)-2) * (len(self.matrix[0])-2)
        for i in range(num):
            result.append(self.oneStep())
        return result

T = int(input())

for t in range(T):
    input1 = input().split(' ')
    row_size = int(input1[0])
    column_size = int(input1[1])
    all = [x for x in input().split(' ')]
    result = []

    mat = []
    mat.append([None for i in range(column_size+2)])
    for i in range(row_size):
        tmp = [all[j] for j in range(i*column_size, (i+1)*column_size)]
        tmp.insert(0,None)
        tmp.append(None)
        mat.append(tmp)
    mat.append([None for i in range(column_size+2)])
    matrix = Matirx(mat)
    result = matrix.go()
    for i in range(len(result)):
        print(result[i]+' ' ,end = '')
    print()
