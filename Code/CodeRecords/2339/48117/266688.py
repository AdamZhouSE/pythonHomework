questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')

    for index in range(len(s)):
        s[index] = int(s[index])

    for i in range(len(s) - 1):
        changeIndex = 0
        temp = 0
        change = False
        reverseNum = set() 
        for j in range(i + 1, len(s)):
            reverseNum.add(s[i])
            if s[j] < s[i]:
                reverseNum.add(s[j])
                
    print(len(reverseNum))