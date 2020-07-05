questNum = int(input())

for quest in range(questNum):
    np = input().split(' ')
    n = int(np[0])
    p = int(np[1])
    s = input().split(' ')

    for i in range(n):
        s[i] = int(s[i])

    hasPrint = False
    for i in range(n):
        if p % s[i] != 0:
            continue
        else:
            restNum = p // s[i]
            if restNum in s[0:i] + s[i + 1:]:
                print('Yes')
                hasPrint = True
                break
    
    if not hasPrint:
        print('No')