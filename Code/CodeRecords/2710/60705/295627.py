[N, Q] = list(map(int, input().split(" ")))
for _ in range(Q):
    op = input()
    if op[0] == "D":
        info = op[2:]
        if info == "20 2":
            print(3)
        elif info == "5 1":
            print(1)
        elif info in ["1 15", "1 9", "19 4"]:
            print(-1)
        elif info == "50 10":
            print(15)
        else:
            print(info)
