size = int(input())
a = 0
while a < size:
    firstStr = input()
    # 将字符串转换成list
    SecondStr = list(input())
    i = 0
    signal = False
    while i < len(firstStr):
        if (firstStr[i] in SecondStr):
            print(firstStr[i])
            signal = True
            break
        i = i + 1
    if not signal:
        print("$")
    a = a + 1