from queue import Queue

fourD = [[1, 0], [-1, 0], [0, -1], [0, 1]]

def solve():
    input()
    newline=input()
    box=[]
    while newline.endswith(','):
        box.append(list(map(int, newline[3:-2].split(','))))
        newline=input()
    box.append(list(map(int, newline[3:-1].split(','))))

    length=len(box)
    width=len(box[0])
    res=0

    for i in range(length):
        for j in range(width):
            lastRes=find(i,j,box)
            if lastRes>res:
                res=lastRes

    print(res)


def find(x,y,box=[]):
    length=len(box)
    width=len(box[0])
    nbox=[[0 for i in range(width)] for j in range(length)]
    global fourD
    res=0
    q=Queue()

    nbox[x][y]=1
    q.put([x,y])
    while not q.empty():
        current=q.get()
        x=current[0]
        y=current[1]
        for i in range(4):
            x1=x+fourD[i][0]
            y1=y+fourD[i][1]
            if x1>=0 and y1>=0 and x1<length and y1<width and nbox[x1][y1]==0:
                if box[x1][y1]>box[x][y] :
                    lastRes=nbox[x][y]+1
                    nbox[x1][y1]=lastRes
                    q.put([x1,y1])
                    if lastRes>res:
                        res=lastRes
    return res

if __name__ == '__main__':
    solve()