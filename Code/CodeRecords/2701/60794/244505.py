a = input()
b = "["
n = (len(a)-len(a.replace(b, "")))//len(b)-1
y = "".join(filter(str.isdigit, a))
m = []
for j in range(n):
    m.append([])
    for i in range(2):
        m[j].append(int(y[j*2+i]))
broad = []
ans = ""
for i in range(3):
    broad.append([])
    for j in range(3):
        broad[i].append(" ")
for i in range(len(m)):
    if i % 2 == 0:
        broad[m[i][0]][m[i][1]] = "x"
    else:
        broad[m[i][0]][m[i][1]] = "o"
for i in range(3):
    if broad[i][0] == broad[i][1] and broad[i][0] == broad[i][2] and broad[i][0] == "x":
        ans = "A"
    if broad[i][0] == broad[i][1] and broad[i][0] == broad[i][2] and broad[i][0] == "o":
        ans = "B"
for i in range(3):
    if broad[0][i] == broad[1][i] and broad[1][i] == broad[2][i] and broad[1][i] == "x":
        ans = "A"
    if broad[0][i] == broad[1][i] and broad[1][i] == broad[2][i] and broad[1][i] == "o":
        ans = "B"
if broad[0][0] == broad[1][1] and broad[1][1] == broad[2][2]:
    if broad[0][0] == "x":
        ans = "A"
    if broad[0][0] == "o":
        ans = "B"
if broad[0][2] == broad[1][1] and broad[2][0] == broad[1][1]:
    if broad[1][1] == "x":
        ans = "A"
    if broad[1][1] == "o":
        ans = "B"
if ans == "":
    o = 0
    for i in range(3):
        for j in range(3):
            if broad[i][j] == " ":
                o = 1
    if o == 1:
        ans = "Pending"
    else:
        ans = "Draw"
print(ans)