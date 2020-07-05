def isRotate(str):
    a = len(str)
    i = 0
    while i < a:
        if str[i] != str[a - 1 - i]:
            return False
        i += 1
    if i == a:
        return True

def notSame(str):
    l = []
    i = 0
    result = 0
    while i < len(str):
        if str[i] in l:
            i += 1
            continue
        else:
            l.append(str[i])
            result += 1
        i += 1
    return result

def rotate(str):
    size = len(str)
    i = 2
    result = notSame(str)
    l = []
    while i <= size:
        j = 0
        while (i + j) <= size:
            if i % 2 == 1 and isRotate(str[j:j + i]):
                if str[j:j + i] in l:
                    j += 1
                    continue
                else:
                    result += 1
                    l.append(str[j:j + i])
            j += 1
        i += 1
    return result

def noRotate(str):
    size = len(str)
    i = 2
    result = 0
    l = []
    while i <= size:
        j = 0
        while (i + j) <= size:
            if i % 2 == 0 or (not isRotate(str[j:j + i])):
                if str[j:j + i] in l:
                    j += 1
                    continue
                else:
                    result += 1
                    l.append(str[j:j + i])
            j += 1
        i += 1
    return result

a = input()
str = input()
result = []
i = 1
x = 0
y = 0
while i <= len(str) - 1:
    x = rotate(str[0:i])
    y = noRotate(str[i:])
    result.append(x * y)
    i += 1
result.sort()
print(result[len(result) - 1])