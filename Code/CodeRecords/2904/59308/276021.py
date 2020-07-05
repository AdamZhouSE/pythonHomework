s = list(input())

if s[0] == '0':
    print(0)
elif s[0] == '-':
    temp = s[1:]
    temp.reverse()
    while True:
        if temp[0] == '0':
            temp.pop(0)
        else:
            break
    print('-'+''.join(temp))
else:
    temp = s
    temp.reverse()
    while True:
        if temp[0] == '0':
            temp.pop(0)
        else:
            break
    print(''.join(temp))


