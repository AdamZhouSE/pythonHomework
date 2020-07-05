moves=eval(input())
wins = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]],
        ]


def checkwin(loc):
    if len(loc)<3:
        return False
    loc.sort(key=lambda x:(x[0],x[1]))
    if loc in wins:
        return True
    return False

A=[]
B=[]
cnt=0
ended=False
for i in range(len(moves)):
    if i % 2 == 0:
        A.append(moves[i])
        if checkwin(A):
            ended=True
            print('A')
            break
    else:
        B.append(moves[i])
        if checkwin(B):
            ended=True
            print('B')
            break
if not ended:
    print("Draw" if len(moves) == 9 else "Pending")