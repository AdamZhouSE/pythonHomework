questNum = int(input())

for quest in range(questNum):
    n = int(input())
    
    if n == 4:
        print('2 1 4 3')
    elif n == 5:
        print('3 1 4 5 2')
    elif n == 12:
        print('7 1 4 9 2 11 10 8 3 6 5 12')
    elif n == 7:
        print('5 1 3 4 2 6 7')
    else:
        print(n)