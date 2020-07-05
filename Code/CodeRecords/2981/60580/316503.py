def manage(a, b, p1, p2, p3):
    result = ''
    if abs(ord(a) - ord(b)) > 26:
        result = a + '-' + b
    elif ord(a) >= ord(b):
        result = a + '-' + b
    elif ord(a) == ord(b) - 1:
        result = a + b
    else:
        if p1 == 1:
            for i in range(ord(a) + 1, ord(b)):
                result = result + chr(i) * p2
        elif p1 == 2 and ord(a) > 58:
            for i in range(ord(a) + 1 - 32, ord(b) - 32):
                result = result + chr(i) * p2
        elif p1 == 2 and ord(a) < 58:
            for i in range(ord(a) + 1, ord(b)):
                result = result + chr(i) * p2
        else:
            for i in range(ord(a) + 1, ord(b)):
                result = result + '*' * p2
        if p3 == 2:
            result = result[::-1]
        result = a + result + b
    return result


p = input().split()
string = input()
mark = [0]
temp = ''
for i in range(len(string)):
    if string[i] == '-':
        temp = temp + string[mark.pop():i - 1]
        if i + 2 < len(string):
            mark.append(i + 2)
        temp = temp + manage(string[i - 1], string[i + 1], int(p[0]), int(p[1]), int(p[2]))
if len(mark) != 0:
    temp = temp + string[mark.pop():]
print(temp)
