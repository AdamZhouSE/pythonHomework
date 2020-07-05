m = int(input().split()[1])
ali = [int(i) for i in input().split()]
ali.insert(0, -666)
for ttt in range(m):
    bli = [int(i) for i in input().split()]

    if bli[0] == 1:
        cli = ali[bli[1]:bli[2] + 1]
        cli.sort()
        print(1+cli.index(bli[3]))

    if bli[0] == 2:
        cli = ali[bli[1]:bli[2] + 1]
        cli.sort()
        print(cli[bli[3]-1])

    if bli[0] == 3:
        ali[bli[1]] = bli[2]

    if bli[0] == 4:
        cli = ali[bli[1]:bli[2] + 1]
        cli = list(set(cli))
        cli.sort(reverse=True)
        for j in cli:
            if j < bli[3]:
                print(j)
                break

    if bli[0] == 5:
        cli = ali[bli[1]:bli[2] + 1]
        cli = list(set(cli))
        cli.sort()
        for j in cli:
            if j > bli[3]:
                print(j)
                break
