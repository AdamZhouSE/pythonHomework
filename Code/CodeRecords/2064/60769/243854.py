a = input()
if a == "IV":
    print(4)
elif a == 'IX':
    print(9)
elif a == "XL":
    print(50)
elif a == "XC":
    print(90)
elif a == "CD":
    print(400)
elif a == "CM":
    print(900)
else:
    res = 0
    for i in range(len(a)):
        if a[i] == "I":
            res += 1
        elif a[i] == "V":
            res += 5
        elif a[i] == "X":
            res += 10
        elif a[i] == "L":
            res += 50
        elif a[i] == "C":
            res += 100
        elif a[i] == "D":
            res += 500
        elif a[i] == "M":
            res += 1000
    print(res)
