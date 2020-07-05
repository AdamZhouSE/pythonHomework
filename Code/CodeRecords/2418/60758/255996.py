tomato=int(input())
chess=int(input())
ham=[]
if(tomato==0 and chess==0):
    print([0,0])
else:
    for little in range(0,chess+1):
        big=chess-little
        if(big*4+little*2==tomato):
            ham.append(big)
            ham.append(little)
            print(ham)
            break
        if(little==chess):
            print("[]")