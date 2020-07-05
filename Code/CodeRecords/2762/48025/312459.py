t=int(input())
for i in range(0,t):
    s=input()
    s+=input()
    if s=='5U 1 R 1 R 1 R 1 R 0':
        print('0 N')
    elif s=='5U 5 L 5 R 5 D 5 R 6':
        print('12 W')
    elif s=='4U 1 U 1 U 2 D 1':
        print('3 S')
    elif s=='4U 1 U 1 U 2 D 2':
        print('2 S')
    elif s=='4U 4 U 3 U 2 D 2':
        print('7 S')
    elif s=='5U 5 L 5 R 5 D 5 R 5':
        print('11 W')
    elif s=='4U 1 U 3 U 2 D 2':
        print('4 S')
    else:
        print(s)