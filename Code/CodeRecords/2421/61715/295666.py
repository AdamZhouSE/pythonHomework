class solution :
    def change() :
        num = str(input())
        Num = list(num)
        for i in range(Num.__len__()) :
            if Num[i] == '6' :
                Num[i] = '9'
                break
        num = "".join(Num)
        print(num)
    change()