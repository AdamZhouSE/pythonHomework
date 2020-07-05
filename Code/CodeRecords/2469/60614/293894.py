for i in range(int(input())):
    str=input()
    while len(str)>0:
        key=str[0]
        if key in str[1:]:
            str=str[1:]
        else:
            break
    while len(str)>0:
        key=str[len(str)-1]
        if key in str[0:len(str)-1]:
            str=str[0:len(str)-1]
        else:
            break
    print(len(str))