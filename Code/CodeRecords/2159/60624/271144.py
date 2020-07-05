def func32():
    n = int(input())
    res = ""
    while n != 0:
        if n >= 1000:
            res += "M"
            n -= 1000
        elif n >= 900:
            res += "CM"
            n -= 900
        elif n >= 500:
            res += "D"
            n -= 500
        elif n >= 400:
            res += "CD"
            n -= 400
        elif n >= 100:
            res += "C"
            n -= 100
        elif n >= 90:
            res += "XC"
            n -= 90
        elif n >= 50:
            res += "L"
            n -= 50
        elif n >= 40:
            res += "XL"
            n -= 40
        elif n >= 10:
            res += "X"
            n -= 10
        elif n >= 9:
            res += "IX"
            n -= 9
        elif n >= 5:
            res += "V"
            n -= 5
        elif n >= 4:
            res += "IV"
            n -= 4
        else:
            res += "I"
            n -= 1
    print(res)
    return
func32()