import sys
from queue import Queue


def solve():
    fourD = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    box=list(map(lambda x:list(map(int,list(x))),map(lambda x:x.replace(' ',''),map(lambda x:x.strip(),sys.stdin.readlines()))))
    length = len(box)
    width = len(box[0])

    def find0(x, y):
        if box[x][y]==0:
            return 0

        nbox = [[-1 for i in range(width)] for j in range(length)]
        q = Queue()

        nbox[x][y] = 0
        q.put([x, y])
        while not q.empty():
            current = q.get()
            x = current[0]
            y = current[1]
            if box[x][y]==0:
                return nbox[x][y]
            for i in range(4):
                x1 = x + fourD[i][0]
                y1 = y + fourD[i][1]
                if x1 >= 0 and y1 >= 0 and x1 < length and y1 < width and nbox[x1][y1] == -1:
                    nbox[x1][y1]=nbox[x][y]+1
                    q.put([x1,y1])

    res=[[0 for i in range(width)]for j in range(length)]

    for i in range(length):
        for j in range(width):
            res[i][j]=find0(i,j)

    output=list(map(lambda x:' '.join((list(map(lambda x:str(x),x)))),res))
    print('\n'.join(output))


if  __name__ == '__main__' :
    solve()