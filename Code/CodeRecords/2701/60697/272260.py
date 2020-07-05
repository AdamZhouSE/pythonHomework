moves=eval(input())

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

flag=True
A, B = set(), set()
for i, (x, y) in enumerate(moves):
    if i % 2 == 0:
        A.add((x, y))
        if checkwin(A):
            print("A")
            flag=False
            break
    else:
        B.add((x, y))
        if checkwin(B):
            print("B")
            flag = False
            break
if(flag):
    if len(moves) == 9 :
        print("Draw")
    else:
        print("Pending")

