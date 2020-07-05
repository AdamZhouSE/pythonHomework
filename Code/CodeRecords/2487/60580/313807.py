size = int(input())
a = 0
while a < size:
    b = input()
    l = input().split()
    l.sort()
    i = 1
    d = {}
    d[l[0]] = 1
    while i <= len(l) - 1:
        if l[i] == l[i - 1]:
            d[l[i]] = d[l[i]] + 1
        else:
            d[l[i]] = 1
        i = i + 1
    dic = sorted(d.items(), key=lambda item: item[1], reverse=True)
    h = str(dic[0][1])
    print(dic[0][0] + " " + h)

    a = a + 1