str = list(input())

number = ''

i = 0
judge = False
while i < len(str):
    if not judge:
        if str[i]==' ' or str[i]=='"':
            i += 1
        elif str[i]=='-':
            judge = True
            number += str[i]
            i += 1
        elif str[i]>='0' and str[i]<='9':
            judge = True
            number += str[i]
            i += 1
        else:
            print(0)
            break
    else:
        if str[i]>='0' and str[i]<='9':
            number += str[i]
            i += 1
        else:
            number = int(number)
            if number <= pow(2,31)-1 and number >= -pow(2,31):
                print(number)
            elif number > pow(2,31)-1:
                print(pow(2,31)-1)
            elif number < -pow(2,31):
                print(-pow(2,31))
            break