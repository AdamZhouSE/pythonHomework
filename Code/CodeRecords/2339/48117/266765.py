questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')

    for index in range(len(s)):
        s[index] = int(s[index])

    reverseNum = []
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[j] < s[i]:
                reverseNum.append(s[j])
                temp = s[j]
                s[j] = s[i]
                s[i] = temp
                
    print(len(reverseNum))