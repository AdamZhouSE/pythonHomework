def int_to_roma():
    num = int(input())
    string = ''
    while num > 0:
        if num >= 1000:
            count = num // 1000
            num = num % 1000
            string += ('M' * count)
        elif num >= 900:
            num -= 900
            string += 'CM'
        elif num >= 500:
            num -= 500
            string += 'D'
        elif num >= 400:
            num -= 400
            string += 'CD'
        elif num >= 100:
            count = num // 100
            num = num % 100
            string += ('C' * count)
        elif num >= 90:
            num -= 90
            string += 'XC'
        elif num >= 50:
            num -= 50
            string += 'L'
        elif num >= 40:
            num -= 40
            string += 'XL'
        elif num >= 10:
            count = num // 10
            num = num % 10
            string += ('X' * count)
        elif num >= 9:
            num -= 9
            string += 'IX'
        elif num >= 5:
            num -= 5
            string += 'V'
        elif num >= 4:
            num -= 4
            string += 'IV'
        else:
            string += ('I' * num)
            num = 0
    return string


print(int_to_roma())