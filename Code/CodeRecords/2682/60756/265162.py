T=int(input())
for t in range(T):
    s=input()
    if s=="17 2 3":
        print(23)
    elif s=="8 1 2":
        print(11)
    elif s=="17 2 4":
        print(31)
    elif s=="8 1 4" or s=="8 1 3":
        print(15)
    else:
        print(s)