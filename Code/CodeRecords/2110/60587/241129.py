inp = int(input())
if inp == 1:
    print('True')
else:
    while inp % 2 == 0:
        inp /= 2
    while inp % 3 == 0:
        inp /= 3
    while inp % 5 == 0:
        inp /= 5
    if inp == 1:
        print('True')
    else: 
        print("False")
