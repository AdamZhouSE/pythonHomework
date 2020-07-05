str = list(input())

number = 0

for i in range(0,len(str)):
    if str[i]=='I':
        number += 1
    if str[i]=='V':
        if i>0 and str[i-1]=='I':
            number += 3
        else:
            number += 5
    if str[i]=='X':
        if i>0 and str[i-1]=='I':
            number += 8
        else:
            number += 10
    if str[i]=='L':
        if i>0 and str[i-1]=='X':
            number += 30
        else:
            number += 50
    if str[i]=='C':
        if i>0 and str[i-1]=='X':
            number += 80
        else:
            number += 100
    if str[i]=='D':
        if i>0 and str[i-1]=='C':
            number += 300
        else:
            number += 500
    if str[i]=='M':
        if i>0 and str[i-1]=='C':
            number += 800
        else:
            number += 1000
print(number)