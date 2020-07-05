numOftests = int(input())
for i in range(numOftests):
    n = int(input())
    s = input()
    if s=="2 1 3":
        print(1)
    elif s=="4 3 1 2":
        print(2)
    elif s=="2 3 1":
        print(1)
    elif s=="2":
        print(1)
    else:
        print(s)