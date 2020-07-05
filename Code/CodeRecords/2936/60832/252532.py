All = int(input())
dic = {}

for q in range(0, All):
    phone = input().strip(' ')
    length = len(phone)
    string = ''
    for x in phone:
        if x == 'A' or x == 'B' or x == 'C':
            string += '2'
        elif x == 'D' or x == 'E' or x == 'F':
            string += '3'
        elif x == 'G' or x == 'H' or x == 'I':
            string += '4'
        elif x == 'J' or x == 'K' or x == 'L':
            string += '5'
        elif x == 'M' or x == 'N' or x == 'O':
            string += '6'
        elif x == 'P' or x == 'S' or x == 'R':
            string += '7'
        elif x == 'V' or x == 'T' or x == 'U':
            string += '8'
        elif x == 'Y' or x == 'W' or x == 'X':
            string += '9'
        elif x == '-':
            continue
        else:
            string += x

    ans = string[:3] + '-' + string[3:]
    if dic.__contains__(ans):
        dic[ans] += 1
    else:
        dic[ans] = 1

get = dic.items()

has = False
for (k, v) in get:
    if v > 1:
        print(k, v)
        has = True

if not has:
    print("No duplicates.",end='')
