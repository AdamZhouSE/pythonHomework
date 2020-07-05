moves = {}
moves = eval(input())
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

def checkwin(S):
    for win in wins:
        flag = True
        for pos in win:
            if pos not in S:
                flag = False
                break
        if flag:
            return True
    return False

[]
A, B = set(), set()
for i in range(len(moves)):
    if i % 2 == 0:
        A.add(tuple(moves[i]))
        if checkwin(A):
            print("A")
            exit()
    else:
        B.add(tuple(moves[i]))
        if checkwin(B):
            print("B")
            exit()
if len(moves) == 9:
    print("Draw")
else:
    print("Pending")
