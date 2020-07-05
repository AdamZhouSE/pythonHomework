

def perfetNum():
    num = int(input())
    factor = []
    if num == 1:
        print(False)
        return
    factor.append(1)
    for j in range(2,num):
        if num % j == 0:
            if j in factor:
                break
            factor.append(j)
            factor.append(num // j)
    if sum(factor) == num:
        print(True)
    else:
        print(False)

perfetNum()
