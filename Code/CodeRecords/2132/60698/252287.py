def test():
    a = list(input())
    result = ''
    while True:
        if isIn(a, 'zero'):
            remove(a, 'zero')
            result = result + '0'
        elif isIn(a, 'one'):
            remove(a, 'one')
            result = result + '1'
        elif isIn(a, 'two'):
            remove(a, 'two')
            result = result + '2'
        elif isIn(a, 'three'):
            remove(a, 'three')
            result = result + '3'
        elif isIn(a, 'four'):
            remove(a, 'four')
            result = result + '4'
        elif isIn(a, 'five'):
            remove(a, 'five')
            result = result + '5'
        elif isIn(a, 'six'):
            remove(a, 'six')
            result = result + '6'
        elif isIn(a, 'seven'):
            remove(a, 'seven')
            result = result + '7'
        elif isIn(a, 'eight'):
            remove(a, 'eight')
            result = result + '8'
        elif isIn(a, 'nine'):
            remove(a, 'nine')
            result = result + '9'
        else:
            break
    print(result)
            

def remove(list_a, s):
    for i in s:
        list_a.remove(i)


def isIn(a, s):
    flag = True
    for i in range(0, len(s)):
        if s[i] not in a:
            flag = False
            break
    return flag


test()
