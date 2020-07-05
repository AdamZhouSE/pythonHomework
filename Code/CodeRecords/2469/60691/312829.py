def getarr(l):
    l1 = []
    for i in range(len(l)):
        if l[i] not in l1:
            l1.append(l[i])
    return l1


def isin(l, l1):
    for i in range(len(l1)):
        if l1[i] not in l:
            return False
    return True


def function(l):
    length = []
    for i in range(len(l)-1):
        for j in range(len(l)):
            if isin(l[i: j+1], getarr(l)):
                length.append(len(l[i:j+1]))
    return min(length)


n = int(input())
string = []
for i in range(n):
    string.append(input())

for i in range(n):
    ltemp = []
    for j in range(len(string[i])):
        ltemp.append(string[i][j])
    print(function(ltemp))

