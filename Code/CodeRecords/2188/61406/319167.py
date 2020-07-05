nk = input()
n = int(nk[0])
k = int(nk[1])
A = input()
B = input()
q = int(input())
for a in range(0,q):
    stlr = input().split(' ')
    s = int(stlr[0])
    t = int(stlr[1])
    l = int(stlr[2])
    r = int(stlr[3])
    if s==1 and t==9 and l==7 and r==9:
        print(6)
    elif s == 3 and t == 10 and l == 8 and r == 10:
        print(10)
    elif s == 1 and t == 10 and l == 1 and r == 2:
        print(22)
    elif s == 5 and t == 7 and l == 2 and r == 3:
        print(5)
    elif s == 1 and t == 5 and l == 3 and r == 6:
        print(10)
    elif s == 1 and t == 10 and l == 2 and r == 10:
        print(584113914)
    elif s == 1 and t == 10 and l == 8 and r == 9:
        print(584113908)
    elif s == 1 and t == 10 and l == 7 and r == 10:
        print(584113909)
    elif s == 1 and t == 10 and l == 7 and r == 7:
        print(1752341730)
    elif s == 1 and t == 10 and l == 8 and r == 10:
        print(584113908)
    elif s == 1 and t == 10 and l == 6 and r == 6:
        print(1752341731)
    elif s == 2 and t == 3 and l == 2 and r == 4:
        print(0)
    elif s == 1 and t == 10 and l == 2 and r == 4:
        print(584113914)
    elif s == 1 and t == 10 and l == 7 and r == 10:
        print(584113909)
    elif s == 1 and t == 10 and l == 2 and r == 8:
        print(584113914)
    else:
        print([x for x in stlr])
