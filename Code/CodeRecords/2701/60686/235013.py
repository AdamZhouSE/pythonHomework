inputStr = input()
inputStr = inputStr[2:len(inputStr) - 2]
arr = inputStr.split("],[")
flagStop = False
moves = []
for i in range(0, len(arr)):
    moves.append("(" + arr[i] + ")")
wins = [
    ['(0,0)', '(0,1)', '(0,2)'],
    ['(1,0)', '(1,1)', '(1,2)'],
    ['(2,0)', '(2,1)', '(2,2)'],
    ['(0,0)', '(1,0)', '(2,0)'],
    ['(0,1)', '(1,1)', '(2,1)'],
    ['(0,2)', '(1,2)', '(2,2)'],
    ['(0,0)', '(1,1)', '(2,2)'],
    ['(0,2)', '(1,1)', '(2,0)'],
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


A, B = set(), set()
for i in range(0, len(moves)):
    if i % 2 == 0:
        A.add(moves[i])
        if checkwin(A):
            print("A")
            flagStop = True
    else:
        B.add(moves[i])
        if checkwin(B):
            print("B")
            flagStop = True
if len(moves) == 9 and not flagStop:
    print("Draw")
elif not flagStop:
    print("Pending")
