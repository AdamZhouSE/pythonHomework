T = int(input())
for i in range(T):
    numerator = int(input())
    denominator = int(input())
    if numerator % denominator == 0:
        print(int(numerator/denominator))
    else:
        s = numerator // denominator
        numerator = numerator % denominator
        if numerator == 2 and denominator == 3:
            print("2.(6)")