def reflecition(x):
    result=""
    while x>=1:
        if x>=1000:
            result += "M"
            x-=1000
        elif x>=900:
            result += "CM"
            x -= 900
        elif x>=500:
            result += "D"
            x-=500
        elif x>=400:
            result += "CD"
            x -= 400
        elif x>=100:
            result += "C"
            x-=100
        elif x>=90:
            result += "XC"
            x -= 90
        elif x>=50:
            result += "L"
            x-=50
        elif x>=40:
            result += "XL"
            x -= 40
        elif x>=10:
            result += "X"
            x-=10
        elif x>=9:
            result += "IX"
            x -= 9
        elif x>=5:
            result += "V"
            x-=5
        elif x>=4:
            result += "IV"
            x -= 4
        elif x>=1:
            result += "I"
            x-=1
    return result


a = int(input())
print(reflecition(a))
