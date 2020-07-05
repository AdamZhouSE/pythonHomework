def is_winner(m):
    for i in range(0, 3):
        if m[i][0] == m[i][1] == m[i][2]:
            return m[i][0]
        if m[0][i] == m[1][i] == m[2][i]:
            return m[0][i]
    if m[0][0] == m[1][1] == m[2][2]:
        return m[0][0]
    if m[2][0] == m[1][1] == m[0][2]:
        return m[0][2]
    return None


s = str(input()).replace(',', '').replace('[', '').replace(']', '')
mat = [([0]*3) for i in range(3)]
index = 0
while index < len(s):
    x = int(s[index])
    y = int(s[index + 1])
    if index % 4 == 0:
        mat[x][y] = "A"
    else:
        mat[x][y] = "B"
    index += 2

if is_winner(mat) == "A":
    print("A")
elif is_winner(mat) == "B":
    print("B")
else:
    if index==18:
        print("Draw")
    else:
        print("Pending")