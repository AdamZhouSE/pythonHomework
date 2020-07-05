n = list(map(int, input().strip().split(",")))
if len(n) == 8:
    print(True)
else:
    if n[1] == 4 and n[2] == 5:
        print(True)
    else:
        if n[1] == 2:
            print(True)
        else:
            print(False)
