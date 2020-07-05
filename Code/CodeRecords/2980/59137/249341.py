def s12():
    string = input()
    order = input().split()
    if order[0] == 'D':
        if order[1] not in string:
            print("no exist")
        else:
            string = string.replace(order[1], "", 1)
    elif order[0] == 'I':
        index = string.rfind(order[1])
        if index == -1:
            print("no exist")
        else:
            seq = (string[0:index], string[index:len(string)])
            string = order[2].join(seq)
    elif order[0] == 'R':
        if order[1] not in string:
            print("no exist")
        else:
            string = string.replace(order[1], order[2])
    print(string)


s12()