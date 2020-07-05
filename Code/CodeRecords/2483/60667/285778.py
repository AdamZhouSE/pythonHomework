t = int(input())
for i in range(t):
    li = list(input())
    patt = input()
    check = False
    for j in li:
        if j in patt:
            print(j)
            check = True
            break
    if not check:
        print('$')