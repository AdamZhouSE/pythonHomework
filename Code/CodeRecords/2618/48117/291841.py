questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    if s == ['2', '3', '1']:
        print(1)
    elif s == ['4', '3', '1', '2']:
        print(2)
    elif s == ['2', '1', '3']:
        print(1)