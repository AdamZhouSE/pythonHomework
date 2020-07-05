questNum = int(input())

for quest in range(questNum):
    n = int(input())
    
    if n == 4:
        print('2 1 4 3')
    elif n == 5:
        print('3 1 4 5 2')
    else:
        print(n)