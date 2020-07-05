def win(chess):
    if chess[0][0] == chess[1][1] and chess[0][0] == chess[2][2] and chess[0][0] != " ":
        return chess[0][0]
    if chess[0][2] == chess[1][1] and chess[0][2] == chess[2][0] and chess[0][2] != " ":
        return chess[0][2]
    for colomn in range(3):
        if chess[colomn][0] != " ":
            if chess[colomn][0] == chess[colomn][1] and chess[colomn][0] == chess[colomn][2]:
                return chess[colomn][0]

    for line in range(3):
        if chess[0][line] != " ":
            if chess[0][line] == chess[1][line] and chess[0][line] ==  chess[2][line]:
                return chess[0][line]

    for colomn in range(3):
        for line in range(3):
            if chess[colomn][line] == " ":
                return "Pending"

    return "Draw"

moves = input()
moves = moves[1:-1]
chess = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

i = 0
step = 0
while i < len(moves):
    if step % 2 == 0:
        player = "A"
    else:
        player = "B"

    colomn = int(moves[i + 1])
    line = int(moves[i + 3])
    chess[colomn][line] = player
    i += 6
    step += 1

print(win(chess))