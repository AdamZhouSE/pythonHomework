def presentation(l1, l2):
    coefficient = l1[0] * l2[0]
    exponent = l1[1] + l2[1]
    result = []
    result.append(coefficient)
    result.append(exponent)

    return result


def createPolynamial(s1):
    l1 = s1.split(' ')

    polynamial = [[]for i in range(len(l1))]

    for i in range(len(l1)):
        polynamial[i].append(int(l1[i]))
        polynamial[i].append(i)

    return polynamial


def polymul(l1, l2):
    temp = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            temp.append(presentation(l1[i], l2[j]))

    temp.sort(key=lambda x: x[1])

    exponent = []
    coefficient = []

    for i in range(len(temp)):
        if not temp[i][1] in exponent:
            exponent.append(temp[i][1])
            coefficient.append(temp[i][0])
        else:
            coefficient[len(coefficient)-1] += temp[i][0]

    for i in range(len(coefficient)-1):
        print(coefficient[i], end='')
        print(' ', end='')
    print(coefficient[len(coefficient)-1])


n = int(input())
length = []
string = [[]for i in range(n)]

for i in range(n):
    length.append(input())
    string[i].append(input())
    string[i].append(input())

for i in range(n):
    polymul(createPolynamial(string[i][0]), createPolynamial(string[i][1]))