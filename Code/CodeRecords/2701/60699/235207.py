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

inp = input()
length = len(inp)
list = []
i = 0
while i <= length - 1:
    temp = []
    while i <= length - 1:
        if inp[i].isdigit():
            temp.append(int(inp[i]))
        elif inp[i] == ']':
            break;
        i += 1
    i += 1
    if (len(temp) != 0):
        list.append(temp)

moves=list
A, B = set(), set()
flag=False
for i, (x, y) in enumerate(moves):
    if i % 2 == 0:
        A.add((x, y))
        if checkwin(A):
            print("A")
            flag=True
    else:
        B.add((x, y))
        if checkwin(B):
            print("B")
            flag=True
if not flag:
    print("Draw" if len(moves) == 9 else "Pending")