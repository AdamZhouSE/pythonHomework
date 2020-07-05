def s21():
    num = int(input())
    for x in range(num):
        number = []
        string = input()
        length = len(string)

        for l in range(1, length+1):
            for i in range(length - l + 1):
                number.append(string[i:i+l])

        product = []
        for n in number:
            pro = 1
            for s in n:
                pro = pro * int(s)
            product.append(pro)

        flag = True
        for p in product:
            if product.count(p) > 1:
                print("0")
                flag = False
                break
        if flag:
            print("1")


s21()