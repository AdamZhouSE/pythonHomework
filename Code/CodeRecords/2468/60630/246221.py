Times = int(input(""))
while Times > 0 :
    Times -= 1

    n = int(input(""))
    num = [int(p) for p in input("").split(' ')]

    product = 1
    for i in num :
        product *= i

    for i in num :
        print(int(product / i), end = " ")
    print()
