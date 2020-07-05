def getFacStr(num):
    string = ''
    for i in range(0,num):
        if i == num - 1:
            string += '1'
        else:
            string += str(num - i) + '*'
    return string


num = int(input())
string = getFacStr(num).split('*')
for i in range(0, num - 1):
    if i % 4 == 0:
        string.insert(i * 2 + 1, '*')
    elif i % 4 == 1:
        string.insert(i * 2 + 1 , '//')
    elif i % 4 == 2:
        string.insert(i * 2 + 1 , '+')
    elif i % 4 == 3:
        string.insert(i * 2 + 1, '-')


print(int(eval(''.join(string))))