

pThree = input().split()
p1 = int(pThree[0])
p2 = int(pThree[1])
p3 = int(pThree[2])
string = input().split('-')
index = 0
# ['abcs', 'w1234', '9s', '4zz']
for i in range(len(string) - 1):
    charLeft = string[i][-1]
    charRight = string[i + 1][0]
    if charLeft.isalpha() and not charRight.isalpha():
        string[i] += '-'
        continue
    else:
        #  如果右边的ascii码更小， 那个保留中间的减号
        if charLeft > charRight:
            string[i] += '-'
            continue
        elif ord(charLeft) + 1 == ord(charRight):
            # 如果只相差一位， 那么不管，只删除减号
            continue
        else:
            stringAdded = ""
            for j in range(ord(charLeft) + 1, ord(charRight)):

                character = chr(j)
                if p1 == 1:
                    # 填充小写字母
                    stringAdded += character * p2
                elif p1 == 2:
                    stringAdded += character.upper() * p2
                else:
                    #  用星号填充
                    stringAdded += '*' * p2
            if p3 == 2:
                stringAdded = stringAdded[::-1]
            string[i] += stringAdded

print(''.join(string))