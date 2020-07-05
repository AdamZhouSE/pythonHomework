def isEven(n, cheat, i, j):
    sum = 0
    res = True
    if (n == 1):
        if (cheat == [[0]] or cheat == [[1]]):
            return True
        elif (j == 0):
            sum = cheat[i][j + 1]
        elif (j == n - 1):
            sum = cheat[i][j - i]
        else:
            sum = cheat[i][j - 1] + cheat[i][j + 1]
    else:
        if (i == 0 and j == 0):
            sum = cheat[i][j + 1] + cheat[i + 1][j]
        elif (i == 0 and j == n - 1):
            sum = cheat[i][j - 1] + cheat[i + 1][j]
        elif (i == n - 1 and j == 0):
            sum = cheat[i - 1][j] + cheat[i][j + 1]
        elif (i == n - 1 and j == n - 1):
            sum = cheat[i][j - 1] + cheat[i - 1][j]
        elif (i == 0):
            sum = cheat[i][j - 1] + cheat[i][j + 1] + cheat[i + 1][j]
        elif (i == n - 1):
            sum = cheat[i][j - 1] + cheat[i][j + 1] + cheat[i - 1][j]
        elif (j == 0):
            sum = cheat[i - 1][j] + cheat[i + 1][j] + cheat[i][j + 1]
        elif (j == n - 1):
            sum = cheat[i - 1][j] + cheat[i + 1][j] + cheat[i][j - 1]
        else:
            sum = cheat[i][j + 1] + cheat[i][j - 1] + cheat[i + 1][j] + cheat[i - 1][j]
    if (sum % 2 == 0):
        return True
    else:
        return False

def chea():
    inp = int(input())
    cheat = []
    for i in range(inp):
        cheat.append(list(input()))
    for i in range(inp):
        for j in range(inp):
            if (cheat[i][j] == "o"):
                cheat[i][j] = 1
            else:
                cheat[i][j] = 0
    for i in range(inp):
        for j in range(inp):
            if (isEven(inp, cheat, i, j) == False):
                return ("NO")
    return ("YES")
print(chea())