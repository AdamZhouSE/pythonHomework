run = int(input())  # 测试用例数量

while run > 0:
    run -= 1
    length = int(input())  # 数组长度
    arr = input().replace(" ", '')
    isApp = False

    tmp = set(arr)
    dic = {x: arr.count(x) for x in tmp}
    for key in dic.keys():
        if dic[key] > length / 2:
            isApp = True
            print(key)
            break

    if not isApp:
        print(-1)
