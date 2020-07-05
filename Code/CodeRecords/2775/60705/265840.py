test = int(input())
for i in range(0, test):
    n = int(input())
    found = False
    for j in range(0, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                if j + k + l == n:
                    print(str(j) + " " + str(k) + " " + str(l))
                    found = True
    if not found:
        print(-1)
