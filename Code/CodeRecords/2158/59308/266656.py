import re
pattern = re.compile('-*[0-9]+')
a = input()
a = a.strip(' ')
if a[0].isdigit() or a[0] == '-':
    a = pattern.findall(a)
    b = ''.join(a)
    if int(b) < -2147483648:
        print(-2147483648)
    elif int(b) > pow(2, 31)-1:
        print(pow(2, 31))
    else:
        print(b)
else:
    print(0)

