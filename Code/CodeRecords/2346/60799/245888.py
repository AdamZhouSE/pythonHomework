class Bug:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = (1, 0)

    def turn(self):
        if self.direction == (1, 0):
            self.direction = (0, 1)
        elif self.direction == (0, 1):
            self.direction = (-1, 0)
        elif self.direction == (-1, 0):
            self.direction = (0, -1)
        elif self.direction == (0, -1):
            self.direction = (1, 0)

    def go(self):
        self.x += self.direction[0]
        self.y += self.direction[1]


class Board:
    def __init__(self, M, N, MAT):
        self.left = -1
        self.right = N
        self.up = -1
        self.down = M
        self.mat = [[MAT[ii * N + jj] for ii in range(M)] for jj in range(N)]
        self.bug = Bug()

    def draw(self):
        print(self.mat[self.bug.x][self.bug.y], end=' ')

    def can_go(self):
        return self.left < self.bug.x + self.bug.direction[0] < self.right \
               and self.up < self.bug.y + self.bug.direction[1] < self.down

    def shrink(self):
        tp = self.bug.direction
        if tp == (1, 0):
            self.left += 1
        elif tp == (0, 1):
            self.up += 1
        elif tp == (-1, 0):
            self.right -= 1
        elif tp == (0, -1):
            self.down -= 1

    def run(self):
        if self.can_go():
            self.draw()
            self.bug.go()
            return True
        else:
            self.bug.turn()
            if self.can_go():
                self.shrink()
                return True
            else:
                self.draw()
                return False


T = int(input())
for i in range(T):
    L = [int(i) for i in input().split(' ')]
    mat = [int(i) for i in input().split()]
    board = Board(L[0], L[1], mat)
    while board.run():
        pass
    print()