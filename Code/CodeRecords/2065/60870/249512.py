Str = input()
Str = Str + ' '
res = ''
i = 0
while i < len(Str):
    if Str[i] == ' ':
        i = i + 1
    else:
        break
if Str[i] != '+' and Str[i] != '-' and Str[i] != ' ' and (Str[i] < '0' or Str[i] > '9'):
    print(0)
elif Str[i] == '-':
    res = res + Str[i]
    i = i + 1
    while '9' >= Str[i] >= '0':
        res = res + Str[i]
        i = i + 1
    if int(res) < int('-' + str(pow(2, 31))):
        print(-2147483648)
    else:
        print(res)
elif '9' >= Str[i] >= '0':
    while '9' >= Str[i] >= '0':
        res = res + Str[i]
        i = i + 1
    if int(res) > int(pow(2, 31) - 1):
        print(2147483647)
    else:
        print(res)
