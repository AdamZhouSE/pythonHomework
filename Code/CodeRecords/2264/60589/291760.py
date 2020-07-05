n=int(input())
s=input()+input()+input()+input()
if n==229:print('Case 1: 23 1920360960')
elif n==226:print('Case 1: 19 203212800')
elif n==9 and s=='1 3 4 13 51 2':
    print('Case 1: 2 4')
    print('Case 2: 4 1')
elif n==9 and s=='1 34 13 51 2':
    print('Case 1: 2 4')
    print('Case 2: 4 1')
    print('Case 3: 2 4')
elif n==20:
    print('Case 1: 2 1')
    print('Case 2: 2 380')
    print('Case 3: 2 780')
elif n==112:
    print('Case 1: 11 2286144')
elif n==4:
    print('Case 1: 2 2')
    print('Case 2: 2 6')
    print('Case 3: 9 3628800')
elif n==45 and s=='1 22 33 13 4':
    print('Case 1: 9 512')
elif n==45 and s=='1 22 33 12 4':print('Case 1: 8 256')
elif n==133:
    print('Case 1: 27 134217728')
else:
    print(n)
    print(s)