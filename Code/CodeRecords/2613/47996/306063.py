T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    connell = 1
    connell_count = 1
    current = 1
    for i in range(1,n+1):
        if i > connell_count:
            connell += 1
            connell_count += connell
        print(current, end="")
        if i == 1:
            current += 1
        elif i == connell_count:
            current += 1
        else:
            current += 2
        if i == n:
            print()
        else:
            print(" ", end="")
