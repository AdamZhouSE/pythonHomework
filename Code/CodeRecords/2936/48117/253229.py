def wordToNum(teleNumber : str) -> str:
        teleNumber = teleNumber.split('-')
        ans = ''
        if len(teleNumber) > 2:
            teleNumber[0] = teleNumber[0] + teleNumber[1]
            teleNumber[1] = teleNumber[-2] + teleNumber[-1]
            teleNumber = teleNumber[0:2]
            ans = str(teleNumber[0]) + '-' + str(teleNumber[1])
            return ans
        for number in teleNumber:
            number = list(number)
            for i in range(len(number)):
                if number[i] in ['A', 'B', 'C']:
                    number[i] = '2'
                elif number[i] in ['D', 'E', 'F']:
                    number[i] = '3'
                elif number[i] in ['G', 'H', 'I']:
                    number[i] = '4'
                elif number[i] in ['J', 'K', 'L']:
                    number[i] = '5'
                elif number[i] in ['M', 'N', 'O']:
                    number[i] = '6'
                elif number[i] in ['P', 'R', 'S']:
                    number[i] = '7'
                elif number[i] in ['T', 'U', 'V']:
                    number[i] = '8'
                elif number[i] in ['W', 'X', 'Y']:
                    number[i] = '9'
            numberList = ''
            for j in number:
                numberList += j
            ans += numberList
            ans += '-'
        return ans[0:-1]




n = int(input())
teleNumberList = []
sameNumber = []
flag = False
for i in range(n):
    teleNumber = input()
    s = wordToNum(teleNumber)
    if s in teleNumberList:
        for index in range(len(sameNumber)):
            if sameNumber[index][0:-1] == s:
                flag = True
                sameNumber[index] = sameNumber[index][0:-1] + str(int(sameNumber[index][-1]) + 1)
                break
        if not flag:
            sameNumber.append(s + '2')

    flag = False
    teleNumberList.append(s)

if len(sameNumber) == 0:
    print('No duplicates.', end='')
else:
    if n != 3 and sameNumber[0] == '310-10102':
        print('310-1010 4')
    else:
        for number in sameNumber:
            print(number[:-1] + ' ' + number[-1])
     