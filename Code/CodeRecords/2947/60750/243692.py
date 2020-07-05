def dealStr():
    num = int(input())
    string = input()
    res = []
    for i in range(0,num):
        request = input().split(' ')
        if request[0] == '1':
            string = string + request[1]
            res.append(string)
        elif request[0] == '2':
            a = int(request[1])
            b = int(request[2])
            string = string[a:a+b]
            res.append(string)
        elif request[0] == '3':
            a = int(request[1])
            string = string[:a] + request[2] + string[a:]
            res.append(string)
        elif request[0] == '4':
            if request[1] not in string:
                res.append(-1)
            else:
                res.append(string.index(request[1]))
    for i in range(0,num):
        print(res[i])


dealStr()