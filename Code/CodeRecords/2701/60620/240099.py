move=eval(input())
wins = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]
def checkwin(x):
    for i in wins:
        flag = True
        for j in i:
            if j not in x:
                flag = False
                break
        if flag:
            return True
    return False
A, B = set(), set()
for i, (x, y) in enumerate(move):
    if i % 2 == 0:
        A.add((x, y))
        if checkwin(A):
            print('A')
    else:
        B.add((x, y))
        if checkwin(B):
            print( "B")
if(len(move)==9):
    print("Draw")
elif(not(checkwin(A)) and not(checkwin(B))):
    print("Pending")