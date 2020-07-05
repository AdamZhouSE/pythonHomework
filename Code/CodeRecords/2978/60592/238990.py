str = input().split(' ')
if str[0]==str[len(str)-1]:
    print(0)
else:
    i = 0
    while i<len(str[0]) and i < len(str[len(str)-1]):
        if str[0][i] == str[len(str)-1][i]:
            continue
        else:
            print(ord(str[0][i])-ord(str[len(str)-1][i]))
            break