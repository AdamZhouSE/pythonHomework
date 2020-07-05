import itertools


def function(s):
    l = s.split(' ')
    count = 0
    result = []

    for i in range(len(l)):
        l[i] = int(l[i])
        count += l[i]

    l.sort()
    for i in range(1, len(l)): #length
        num1 = list(itertools.combinations(l, i))
        
        for m in range(len(num1)):
            tempcount = 0
            for j in range(len(num1[m])):
                tempcount += list(num1[m])[j]
            result.append(abs(count-2*tempcount))

    return min(result)


n = int(input())
num = []
string = []

for i in range(n):
    num.append(input())
    string.append(input())

for i in range(n):
    print(function(string[i]))