def cal(str1):
    list = []
    for i in range(len(str1)):
        if str1[i].isalpha():
            if not str1[i].isupper():
                list.append(chr(ord('z') - (ord(str1[i]) - ord('a'))))
            else:
                list.append(chr(ord('Z') - (ord(str1[i]) - ord('A'))))
        else:
            list.append(str1[i])

    return "".join(list)
while True:
    a = input()
    if a == '!':
        break
    print(cal(a))
