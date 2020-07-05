def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def isValid(l):
    t = sorted(set(l))
    if len(t) == 1:
        return True
    elif len(t) == 2:
        if (t[1] - t[0]) % 2 == 0:
            return True
        else:
            return False
    elif len(t) == 3:
        if t[2] - t[1] == t[1] - t[0]:
            return True
        else:
            return False
    else:
        return False

input()
l = getInput()
t = isValid(l)

if t == True:
    print('YES')
else:
    print('NO')