import itertools

t = int(input())
A = []
for x in range(0, t):
    A.append(input())


def func1(string):
    a = []
    b = []
    c = []
    index = 0
    while index < len(string):
        if string[index] == "a" or string[index] == "e" \
                or string[index] == "i" or string[index] == "o" or string[index] == "u":
            a.append(index)
        else:
            b.append(index)
        index += 1
    if len(a) == 0 or len(b) == 0:
        print(-1)
    elif a[0] > b[len(b) - 1]:
        print(-1)
    else:
        for indexa in a:
            for indexb in b:
                if indexa < indexb:
                    lst = func2(string, indexa, indexb)
                    for x in lst:
                        c.append(string[indexa] + x + string[indexb])
                    c.append(string[indexa] + string[indexb])
    c_1=[]
    for x in c:
        if x not in c_1:
            c_1.append(x)
    c_1.sort()
    index = 0
    while index < len(c_1):
        if index == len(c_1)-1:
            print(c_1[index])
        else:
            print(c_1[index], end=" ")
        index += 1
    return


def func2(string, indexa, indexb):
    newstring = string[indexa + 1:indexb]
    lst = []
    for i in range(1, len(newstring) + 1):
        lst1 = [''.join(x) for x in itertools.combinations(newstring, i)]
        lst += lst1
    return lst


for x in A:
    func1(x)
