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
    x = 0
    for j in range(len(e[i])):
        if e[i][j] == "" or e[i][j] == "a" or e[i][j] == "e" or e[i][j] == "i" or e[i][j] == "o" or e[i][j] == "u":
            continue
        else:
            x = x + 1
    if x % 2 == 0:
        print("SHE!")
    else:
        print("HE!")