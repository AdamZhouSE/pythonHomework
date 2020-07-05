def function(l):
    l1 = []
    for i in range(len(l)):
        if not l[i] in l1:
            l1.append(l[i])

    lresult = [[]for i in range(len(l1))]
    for i in range(len(l1)):
        lresult[i].append(l1[i])
        lresult[i].append(l.count(l1[i]))

    lresult.sort(key=lambda x: x[1], reverse=True)

    ltemp = []
    for i in range(len(lresult)):
        for j in range(lresult[i][1]):
            ltemp.append(lresult[i][0])
    return ltemp


n = int(input())
num = []
string = []

for i in range(n):
    num.append(int(input()))
    string.append(input())

for i in range(n):
    ltemp = list(map(int, string[i].split(' ')))

    for j in range(len(ltemp)-1):
        print(function(ltemp)[j], end='')
        print(' ', end='')
    print(function(ltemp)[len(ltemp)-1])






