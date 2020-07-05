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
    # 按字典里的value升序排序
    dict = sorted(d.items(), key=lambda item: item[1])
    # 遍历字典每一项
    # d.items: an iterator over the (key, value) items
    h = 0
    for key, value in d.items():
        if (num >= value):
            num = num - value
        else:
            h = h + 1
    print(h)
    a = a + 1