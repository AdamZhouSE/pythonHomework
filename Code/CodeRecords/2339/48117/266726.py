questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')

    for index in range(len(s)):
        s[index] = int(s[index])

    reverseNum = set()
    for i in range(len(s) - 1):
        reverseNum.add(s[i])
        for j in range(i + 1, len(s)):
            if s[j] < s[i]:
                reverseNum.add(s[j])
                temp = s[j]
                s[j] = s[i]
                s[i] = temp


    print(len(reverseNum))