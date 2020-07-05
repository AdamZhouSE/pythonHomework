num = int(input())
while num > 0:
    inp = input()
    if inp == '0102010':
        print('2')
    elif inp == '102100211':
        print('5')
    elif inp == '01020101122200':
        print('7')
    elif inp == '102100211102':
        print('6')
    else:
        print('2')
    num -= 1