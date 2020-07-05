questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')

    count0 = 0
    for i in range(n):
        if s[i] == '0':
            count0 += 1
        else:
            print(s[i], end=' ')

    if count0 == 0:
        print()
    else:
        for j in range(count0):
            if j != count0 - 1:
                print('0', end=' ')
            else:
                print('0 ')