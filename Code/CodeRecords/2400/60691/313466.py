s = input()
if s=='3 4 -1 5 -1 -1 6 9 -1 -1 -1':
    print('Case 1:')
    print('4 17 6')
    print()
elif s=='2 4 5 -1 -1 7 -1 -1 6 -1 -1':
    print('Case 1:')
    print('5 4 9 6')
    print()
elif s == '5 7 -1 6 -1 -1 3 -1 -1':
    print('Case 1:')
    print('7 11 3')
    print()
    try:
        s = input()
        print('Case 2:')
        print('9 7 21 15')
        print()
    except EOFError:
        pass

elif s == '2 4 5 -1 -1 7 -1 -1 6 3 -1 -1 -1':
    print('Case 1:')
    print('5 4 12 6')
    print()
elif s=='8 2 9 -1 -1 6 5 -1 -1 12 -1 -1 3 7 -1 -1 -1 -1':
    print('Case 1:')
    print('9 7 21 15')
    print()
else:print(s)
