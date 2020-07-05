from queue import Queue


def solve():
    input()
    newline=input()
    box=[]
    while newline.endswith(','):
        box.append(list(map(int, newline[2:-2].split(','))))
        newline=input()
    box.append(list(map(int, newline[2:-1].split(','))))
    length = len(box)
    width = len(box[0])

    def findpath(begin,end):
        fourD = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        nbox = [[-1 for i in range(width)] for j in range(length)]
        q = Queue()

        if begin==end:
            return 0

        nbox[begin[0]][begin[1]] = 0
        q.put(begin)
        while not q.empty():
            current = q.get()
            x = current[0]
            y = current[1]
            if x==end[0] and y==end[1]:
                return nbox[x][y]
            for i in range(4):
                x1 = x + fourD[i][0]
                y1 = y + fourD[i][1]
                if x1 >= 0 and y1 >= 0 and x1 < length and y1 < width and nbox[x1][y1] == -1 and box[x1][y1]!=0:
                    nbox[x1][y1]=nbox[x][y]+1
                    q.put([x1,y1])
        return -1

    def nex():
        res=[-1,-1]
        shortest=255
        for i in range(length):
            for j in range(width):
                if box[i][j]>1 and box[i][j]<shortest:
                    res=[i,j]
                    shortest=box[i][j]
        return res

    def cutDown(point):
        box[point[0]][point[1]]=1

    nextTree=nex()
    resAll=0
    current=[0,0]
    while nextTree!=[-1,-1]:
        path=findpath(current,nextTree)
        if path==-1:
            resAll=-1
            break
        resAll+=path
        current = nextTree
        cutDown(nextTree)
        nextTree=nex()
    print(resAll)

if __name__ == '__main__':
    solve()