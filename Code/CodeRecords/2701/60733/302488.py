def tictactoe(moves) -> str:
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

    A, B = set(), set()
    for i, (x, y) in enumerate(moves):
        if i % 2 == 0:
            A.add((x, y))
            if checkwin(A):
                return "A"
        else:
            B.add((x, y))
            if checkwin(B):
                return "B"

    return "Draw" if len(moves) == 9 else "Pending"


s = input().replace(",", " ").replace("[", "").replace("]", "")
l = list(s.split())
length = len(l)
move = [[0 for i in range(2)] for j in range(length//2)]

for i in range(0, length, 2):
    move[i // 2][0] = int(l[i])
    move[i // 2][1] = int(l[i + 1])
res = tictactoe(move)
print(res)
