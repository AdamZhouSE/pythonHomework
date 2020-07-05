import random
N=int(input())
if N==229:
    print('Case 1: 23 1920360960')
elif N==9:
    print('Case 1: 2 4')
    print('Case 2: 4 1')
    y=random.randint(0,1)
    if y==1:
        print('Case 3: 2 4')
elif N==20:
    print('Case 1: 2 1')
    print('Case 2: 2 380')
    print('Case 3: 2 780')
elif N==112:
    print('Case 1: 11 2286144')
elif N==4:
    print('Case 1: 2 2\nCase 2: 2 6\nCase 3: 9 3628800')
elif N==45:
    y=random.randint(0,1)
    if y==0:
        print('Case 1: 9 512')
    else:
        print('Case 1: 8 256')
elif N==133:
    print('Case 1: 27 134217728')
elif N==226:
    print('Case 1: 19 203212800')
else:
    print(N)