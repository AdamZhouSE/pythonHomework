def validnumber(x):
    if isinteger(x):
        return True
    elif x.find('e')!=-1:
        return scientific(x)
    elif x.find('.')!=-1:
        return decimal(x)
    else:
        return False


def isinteger(x):
    if x.isdecimal():
        return True
    elif x=='':
        return False
    elif x[0]=='-':
        x = x[1:]
        return x.isdecimal()
    else:
        return False


def decimal(x):
    t = x.split('.')
    if t[0].isdecimal() and t[1].isdigit():
        return True
    else:
        return False


def scientific(x):
    list1 = x.split('e')
    if isinteger(list1[0]) or decimal(list1[0]):
        if isinteger(list1[1]):
            return True
        else:
            return False
    else:
        return False


source = input()
print(validnumber(source))
    