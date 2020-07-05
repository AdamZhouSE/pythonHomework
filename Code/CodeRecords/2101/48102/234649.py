def happy_number():
    num = int(input())
    if num == 1:
        print(True)
        return
    elif num < 10:
        print(False)
        return
    s = set()
    while True:
        num = sum(int(i) ** 2 for i in str(num))
        if num == 1:
            print(True)
            return
        elif num in s:
            print(False)
            return
        else:
            s.add(num)


happy_number()