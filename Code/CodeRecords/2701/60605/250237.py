
def solve() -> str:
    steps = list(eval(input()))
    table = [[" " for j in range(3)] for i in range(3)]
    currentPerson = "A"
    for i in steps:
        table[i[0]][i[1]] = currentPerson
        if currentPerson == "A": currentPerson = "B"
        else: currentPerson = "A"
    # print(table)
    # Check rows
    for i in range(3):
        if table[i][0] == table[i][1] and table[i][0] == table[i][2] and table[i][0] != " ":
            return table[i][0]
    # Check cols
    for i in range(3):
        if table[0][i] == table[1][i] and table[0][i] == table[2][i] and table[0][i] != " ":
            return table[0][i]
    # Check digs
    if table[0][0] == table[1][1] and table[0][0] == table[2][2]  and table[1][1] != " ":
        return table[0][0]
    if table[0][2] == table[1][1] and table[1][1] == table[2][0]  and table[1][1] != " ":
        return table[1][1]

    if len(table) < 9: return "Pending"
    return "Draw"

if __name__ == '__main__':
    print(solve())
