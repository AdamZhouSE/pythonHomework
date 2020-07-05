size = int(input())
a = 0
while a < size:
    b = input()
    list = input().split()
    num = int(input())
    i = 0
    d = {}
    while i < len(list):
        if (list[i] in d):
            d[list[i]] = d[list[i]] + 1
        else:
            d[list[i]] = 1
        i = i + 1
    dict = sorted(d.items(), key=lambda item: item[1])
    h = 0
    for key, value in d.items():
        if (num >= value):
            num = num - value
        else:
            h = h + 1
    print(h)
    a = a + 1