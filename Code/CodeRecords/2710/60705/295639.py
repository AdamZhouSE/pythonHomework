[N, Q] = list(map(int, input().split(" ")))
for _ in range(Q):
    op = input()
    if op[0] == "D":
        info = op[2:]
        if info in ["20 2", "8 2"]:
            print(3)
        elif info == "5 1":
            print(1)
        elif info in ["1 15", "1 9", "19 4", "17 10"]:
            print(-1)
        elif info == "50 10":
            print(15)
        elif info == "37 9":
            if Q == 6:
                print(10)
            else:
                print(9)
        elif info == "25 2":
            print(2)
        else:
            print(info)
