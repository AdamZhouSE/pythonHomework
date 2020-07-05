rome = input()
length = len(rome)
digital = 0
for i in range(0, length):
    a = rome[i]
    if a == 'M':
        digital += 1000
    elif a == 'D':
        digital += 500
    elif a == 'C':
        if i<length-1 and (rome[i + 1] == 'D' or rome[i + 1] == 'M'):
            digital -= 100
        else:
            digital += 100
    elif a == 'L':
        digital += 50
    elif a == 'X':
        if i<length-1 and (rome[i + 1] == 'C' or rome[i + 1] == 'L'):
            digital -= 10
        else:
            digital += 10
    elif a == 'V':
        digital += 5
    else:
        if i<length-1 and (rome[i + 1] == 'X' or rome[i + 1] == 'V'):
            digital -= 1
        else:
            digital += 1
print(digital)