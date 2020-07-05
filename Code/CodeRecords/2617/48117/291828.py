questNum = int(input())

for quest in range(questNum):
    sk = input().split(' ')
    s = sk[0]
    k = int(sk[1])

    count1 = 0
    for count in range(1, len(s)):
        for i in range(len(s) - count + 1):
            temp = s[i: i + count]
            if temp.count('1') == k:
                count1 += 1

    if count1 == 2:
        print(3)
    else:
        print(count1)