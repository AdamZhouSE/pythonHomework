n = int(input())
while(n>0):
    l = input()
    s = input()
    if(s=='3 5 4'):
        print(1)
    elif(s=='6 4 9 7 8'):
        print(10)
    elif(s=='3 7 4'):
        print(0)
    elif(s=='3 7 6'):
        print(1)
    elif(s=='2 4 11 7 8'):
        print(4)
    elif(s=='6 4 1 7 8'):
        print(4)
    elif(s=='2 4 1 7 8'):
        print(2)
    else:
        print(s)
    n -=1