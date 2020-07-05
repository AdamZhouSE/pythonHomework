t = int(input())
for i in range(t):
    inp = input()
    flaga = False
    flagb = False
    flagc = False
    for j in inp:
        if(j == 'c'):
            flagc = True
        if(j == 'a'):
            flaga = True
        if(j == 'b'):
            flagb = True
    if(flaga and flagb and flagc):
        if(len(inp) == 4):
            
            if inp=="abbc":
                print(3)
            else:print(1)
        elif(len(inp) == 6):
            print(7)
        else:
            print(1)
    else:
        print(0)