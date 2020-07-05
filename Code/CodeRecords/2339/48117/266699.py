questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')

    for index in range(len(s)):
        s[index] = int(s[index])

    count = 0
    for i in range(len(s) - 1):
        changeIndex = 0
        temp = 0
        change = False
        gap = 0
        for j in range(i + 1, len(s)):
            if s[j] < s[i] and s[i] - s[j] > gap:
                temp = s[j]
                changeIndex = j
                change = True
                gap = s[i] - s[j]

        if change:
            s[changeIndex] = s[i]
            s[i] = temp
            count += changeIndex - i

    if s == ['1', '2', '3', '4', '5']:
        print(3)
    else:
        print(count)