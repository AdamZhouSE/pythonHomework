str = list(input())

number = 0

for i in range(0,len(str)):
    if str[i]=='I':
        number += 1
    if str[i]=='V':
        if number < 5:
            number = 5 - number
        else:
            number += 5
    if str[i]=='X':
        if number < 10:
            number = 10 - number
        else:
            number += 10
    if str[i]=='L':
        if number < 50:
            number = 50 - number
        else:
            number += 50
    if str[i]=='C':
        if number < 100:
            number = 100 - number
        else:
            number += 100
    if str[i]=='D':
        if number < 500:
            number = 500 - number
        else:
            number += 500
    if str[i]=='M':
        if number < 1000:
            number = 1000 - number
        else:
            number += 1000
print(number)