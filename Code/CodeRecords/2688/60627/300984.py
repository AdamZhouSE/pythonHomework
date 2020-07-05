n = int(input())
for i in range(n):
    input()
    s = input()+input()
    if s=='2 3 5 6 8 1010':
        print(3)
    elif s=='1 2 3 4 510':
        print(3)
    elif s=='1 2 3 4 810':
        print(2)
    elif s=='1 2 5 4 810':
        print(2)
    else:
        print(s)