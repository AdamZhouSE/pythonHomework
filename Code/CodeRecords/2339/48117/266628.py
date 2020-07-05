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
        for j in range(i + 1, len(s)):
            if s[j] < s[i]:
                temp = s[j]
                changeIndex = j
                gap = s[i] - s[j]
        s[changeIndex] = s[i]
        s[i] = temp
        count += j - i

    print(count)