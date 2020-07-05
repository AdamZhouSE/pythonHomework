str = input()

number = int(str)

answer = ''

while number > 0:
    if number >= 1000:
        answer += 'M'
        number -= 1000
    elif number >= 900:
        answer += 'CM'
        number -= 900
    elif number >= 500:
        answer += 'D'
        number -= 500
    elif number >= 400:
        answer += 'CD'
        number -= 400
    elif number >= 100:
        answer += 'C'
        number -= 100
    elif number >= 90:
        answer += 'XC'
        number -= 90
    elif number >= 50:
        answer += 'L'
        number -= 50
    elif number >= 40:
        answer += 'XL'
        number -= 40
    elif number >= 10:
        answer += 'X'
        number -= 10
    elif number >= 9:
        answer += 'IX'
        number -= 9
    elif number >= 5:
        answer += 'V'
        number -= 5
    elif number >= 4:
        answer += 'IV'
        number -= 4
    elif number >= 1:
        answer += 'I'
        number -= 1
    else:
        break
        
 print(answer)