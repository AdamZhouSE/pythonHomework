questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s1 = input().split(' ')
    s2 = input().split(' ')

    for i in range(n):
        s1[i] = int(s1[i])
        s2[i] = int(s2[i])

    s1 = sorted(s1)
    s2 = sorted(s2)

    if s1 == s2:
        print(1)
    else:
        print(0)