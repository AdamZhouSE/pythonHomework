import re

s = input()
i = input()
j = i.split()


def delete(w):
    global s
    temp = ''
    for i, e in enumerate(s):
        if e != w:
            temp += e
        else:
            if i < len(s):
                temp += s[i + 1:]
            else:
                pass
            return temp
    return temp


def insert(a1, a2):
    global s
    temp = ''
    l = list(s)
    m = list(s)
    temp2 = list(s)
    for i, e in enumerate(s):
        if e == a1:
            l.insert(i, a2)
            temp2 = l
            l = list(s)
    temp = (''.join(temp2))
    return temp


def replace(a1, a2):
    global s
    temp = re.sub(a1, a2, s)
    return temp

def myprint(temp):
    global s
    if temp == s:
        print("no exist")
        print(s)
    else:
        print(temp)


if len(j) == 2:
    myprint(delete(j[1]))
else:
    if j[0] == 'I':
        myprint(insert(j[1], j[2]))
    if j[0] == 'R':
        myprint(replace(j[1], j[2]))