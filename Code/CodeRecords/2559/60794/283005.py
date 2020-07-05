num = int(input())
e = []
temp = 0
for i in range(num):
    e.append(list(input()))
for i in range(num):
    for j in range(len(e[i])):
        for k in range(j+1, len(e[i])):
            if e[i][j] == e[i][k]:
                e[i][k] = ""
for i in range(num):
    for j in range(len(e[i])):
        if e[i][j] == "":
            temp = 1
            break
    if temp == 1:
        print(0)
    else:
        print(1)
    temp = 0