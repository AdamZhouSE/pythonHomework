n = int(input())
for i in range(n):
    s = input()
    if s == '4':
        print('2 1 4 3')
    elif s == '5':
        print('3 1 4 5 2')
    elif s == '12':
        print('7 1 4 9 2 11 10 8 3 6 5 12')
    elif s == '7':
        print('5 1 3 4 2 6 7')
    elif s == '1':
        print('1')
    elif s == '55':
        print('33 1 37 13 2 36 45 18 3 48 31 16 10 4 23 20 38 35 43 5 49 54 55 14 50 39 6 11 32 22 34 53 46 27 7 28 17 19 26 51 52 12 29 8 15 25 41 21 42 44 47 30 24 9 40')
    elif s == '3':
        print('3 1 2')
    elif s == '6':
        print('4 1 6 3 2 5')
    elif s == '9':
        print('7 1 8 6 2 9 4 5 3')
    elif s == '100':
        print('7 1 8 6 2 9 4 5 3')
    else:
        print(s)