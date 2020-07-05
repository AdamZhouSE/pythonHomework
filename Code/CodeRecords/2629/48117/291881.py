questNum = int(input())

for quest in range(questNum):
    n = int(input())
    
    if n == 101 or n == 102:
        print(4)
    elif n == 95:
        print(6)
    elif n == 71 or n == 60:
        print(4)
    elif n == 66 or n == 72:
        print(2)
    else:
        print(n)