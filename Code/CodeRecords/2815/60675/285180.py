def strtoInt(string:str)-> int:
    return int(string)

def func(l: list) -> int:
    isNeg, isPos, step, isZero, isPosandleast = 0, 0, 0, 0, 10000
    for i in l :
        if i < 0:
            isNeg += 1
            step += (-1 - i)
        elif i > 0:
            isPos += 1
            step += (i - 1)
            if i < isPosandleast:
                isPosandleast = i
        else :  # 0 假设向正加成1
            isZero += 1
    if isNeg % 2 == 0:
        return step + isZero
    else:
        if isPos != 0 and isZero == 0:
            return step + 2 + isZero
        else:
            return step + isZero

n = int(input())
l = list(map(strtoInt, input().strip().split(" ")))
print(func(l))
