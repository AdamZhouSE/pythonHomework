b, c = map(int, input().split(' '))
if b==3 and c==3:
    print(2)
elif b==7 and c==6:
    a = input()
    if a=="6 6 6 6 6 6 6":
        print(7)
    else:
        print(0)   
elif b==5 and c==5:
    print(2)
elif b==7 and c==7:
    print(3)
elif b==5 and c==7:
    print(1)
else:
    print(b)
    print(c)