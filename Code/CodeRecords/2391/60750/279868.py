def sign():
    n = int(input())
    names = []
    for i in range(0,n):
        names.append(input())
    m = int(input())
    res = []
    ask = []
    for i in range(0,m):
        student = input()
        if student in names:
            if student in ask:
                res.append('REPEAT')
            else:
                res.append('OK')
                ask.append(student)
        else:
            res.append('WRONG')
    for i in range(0,m):
        print(res[i])


sign()
