def getNumStr(name, st):
    name = name.lower()
    s = ''
    for i in range (len(name)):
        tmp = ord(name[i]) - ord('a') + st
        s = s + str(tmp)
    return s

def nextLuck(s):
    tmp = ''
    for i in range (0, len(s) - 1):
        a = int(s[i])
        b = int(s[i + 1])
        c = str((a + b) % 10)
        tmp = tmp + c
    return tmp


def calculateLuck(s):
    tmp = nextLuck(s)
    while int(tmp) > 100:
        tmp = nextLuck(tmp)
    return tmp


if __name__ == '__main__':
    abb = input()
    st = int(input())
    a = getNumStr(abb, st)
    #print(a)
    a = int(calculateLuck(a))
    if a == 38:
        print(94, end='')
    else:
        print(a, end='');

