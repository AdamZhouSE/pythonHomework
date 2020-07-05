num = int(input())
a = []
b = []
for i in range(num):
    temp = input()
    a.append(input().split(" "))
    b.append(input().split(" "))
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(j+1, len(a[i])):
            if a[i][j] == a[i][k]:
                a[i][k] = ""
for i in range(len(b)):
    for j in range(len(b[i])):
        for k in range(j+1, len(b[i])):
            if b[i][j] == b[i][k]:
                b[i][k] = ""
for i in range(num):
    ans = 0
    for j in range(len(a[i])):
        if a[i][j] == "":
            continue
        ans = ans + 1
    for j in range(len(b[i])):
        x = 0
        if b[i][j] == "":
            continue
        for k in range(len(a[i])):
            if b[i][j] == a[i][k]:
                x = 1
                break
        if x == 0:
            ans = ans + 1
    print(ans)