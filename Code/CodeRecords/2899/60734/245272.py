def isExponential(x):
    if x>1:
        if x%4 == 0:
            return isExponential(x/4)
        else:
            return False
    return True

if isExponential(int(input())):
    print('true')
else:
    print('false')