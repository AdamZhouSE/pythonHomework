str = input()

def analyse(str):
    result = ''
    has_sign = False
    for s in str:
        if s == ' ':
            if result != '':
                break
        elif s == '+':
            if has_sign:
                break
            else:
                has_sign = True
        elif s == '-':
            if has_sign:
                break
            else:
                result += '-'
                has_sign = True
        elif ord('0') <= ord(s) <= ord('9'):
            result += s
        else:
            break
    return result if result!='' else '0'

result = int(analyse(str))
if result > pow(2,31)-1 :
    print(pow(2,31)-1)
elif result < pow(2,31)*-1:
    print(pow(2,31)*(-1))
else:
    print(result)



