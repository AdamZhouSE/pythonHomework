def func3():
    num = int(input())
    array = []
    while num > 0:
        num -= 1
        tem1 = int(input())
        tem2 = 0
        while tem1 > 0:
            tem3 = 1
            for i in range(0, 5):
                tem3 *= tem1
            tem2 += tem3
            tem1 -= 1
        array.append(tem2)
    for item in array:
        print(item)
func3()