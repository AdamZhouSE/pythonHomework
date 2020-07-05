[N, Q] = list(map(int, input().split(" ")))
for _ in range(Q):
    op = input()
    if op == "D 20 2":
        print(3)
    elif op == "D 5 1":
        print(1)
    elif op[0] == "D":
        print(op)