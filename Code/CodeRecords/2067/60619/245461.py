def trans_to_roma(i):
    if i == 0:
        return ""
    elif i >= 1000:
        return "M" + trans_to_roma(i - 1000)
    elif i >= 900:
        return "CM" + trans_to_roma(i - 900)
    elif i >= 500:
        return "D" + trans_to_roma(i - 500)
    elif i >= 400:
        return "CD" + trans_to_roma(i - 400)
    elif i >= 100:
        return "C" + trans_to_roma(i - 100)
    elif i >= 90:
        return "XC" + trans_to_roma(i - 90)
    elif i >= 50:
        return "L" + trans_to_roma(i - 50)
    elif i >= 40:
        return "XL" + trans_to_roma(i - 40)
    elif i >= 10:
        return "X" + trans_to_roma(i - 10)
    elif i >= 9:
        return "IX" + trans_to_roma(i - 9)
    elif i >= 5:
        return "V" + trans_to_roma(i - 5)
    elif i >= 4:
        return "IV" + trans_to_roma(i - 4)
    else:
        return "I" + trans_to_roma(i - 1)


target = int(input())
print(trans_to_roma(target))
