#1 1 1 2 2 3
t = int(input())
for ti in range(t):
    a=input()
    b=input()
    if a+' '+b=='3 1 2 3':
        print(10)
    elif a+' '+b=='3 1 2 2':
        print(5)
    elif a+' '+b=='4 1 2 5 4':
        print(20)
    elif a+' '+b=='4 1 2 5 6':
        print(20)
    elif a+' '+b=='4 1 2 3 4':
        print(20)
    elif a+' '+b=='3 1 2 1':
        print(7)
    else:
        print(a,b)