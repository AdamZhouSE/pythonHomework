import itertools


def isproper(l):
    if len(l) == 1:
        return True
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return False
    return True


def adujustment(l, n):
    s = ''
    for i in range(len(l)):
        s += l[i]

    if n == 0:
        if isproper(l):
            return True
        else:
            return False
    elif n == 1:
        for i in range(len(l)):
            temp = []
            for i in range(len(s)):
                temp.append(s[i])
            temp.pop(i)
            if isproper(temp):
                return True
        return False
    else:
        l1 = []
        for i in range(len(l)):
            l1.append(i)

        ladjust = list(itertools.combinations(l1, n))

        for i in range(len(ladjust)):
            temp = []
            for m in range(len(s)):
                temp.append(s[m])

            for j in range(n):
                temp.pop(list(ladjust[i])[j]-j)

            if isproper(temp):
                return True

        return False


def function(l):
    for i in range(len(l)):
        if adujustment(l, i):
            return i


n = int(input())
s = input()

l = []
for i in range(len(s)):
    l.append(s[i])

print(function(l))







