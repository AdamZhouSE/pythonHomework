test = int(input())
for i in range(0, test):
    n = int(input())
    found = False
    for j in range(0, n):
        if j + j + 1 + j + 2 == n:
            print(str(j) + " " + str(j+1) + " " + str(j+2))
            found = True
            break
    if not found:
        print(-1)
