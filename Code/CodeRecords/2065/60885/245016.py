num = input().lstrip()
if num[0] != '-' and not num[0].isdigit():
    print(0)
else:
    result = ''
    if num[0] == '-':
        result += num[0]
        num = num[1:]
    for c in num:
        if c.isdigit():
            result += c
        else:
            break
    result = int(result)
    if result > pow(2, 31)-1:
        print(pow(2,31)-1)
    elif result < -pow(2, 31):
        print(-pow(2,31))
    else:
        print(result)