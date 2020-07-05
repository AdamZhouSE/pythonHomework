def function(l):
    l1 = []
    for i in range(len(l)):
        if not l[i] in l1:
            l1.append(l[i])

    lresult = [[]for i in range(len(l1))]
    for i in range(len(l1)):
        lresult[i].append(l1[i])
        lresult[i].append(l.count(l1[i]))
    lresult.sort(key=lambda x : x[0])
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

strarr = []
for i in range(n-1):
    ltemp = list(map(int, string[i].split(' ')))
    string1 = ''

    for j in range(len(ltemp)-1):
        string1 += str(function(ltemp)[j])
        string1 += ' '
    string1 += str(function(ltemp)[len(ltemp)-1])
    strarr.append(string1)

ltemp = list(map(int, string[n-1].split(' ')))
string1 = ''
for j in range(len(ltemp)-1):
    string1 += str(function(ltemp)[j])
    string1 += ' '
string1 += str(function(ltemp)[len(ltemp)-1])
strarr.append(string1)

for i in range(len(strarr)):
    print(strarr[i])














