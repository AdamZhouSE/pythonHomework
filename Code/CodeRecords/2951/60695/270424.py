def twoToTen(two):
    n = len(two)
    re = 0
    for i in range(0, n):
        re += int(two[i])*(2**(n-i-1))
    return re

def threeToTen(three):
    n = len(three)
    re = 0
    for i in range(0, n):
        re += int(three[i])*(3**(n-i-1))
    return re

two = input()
three = input()
t2 = []
t3 = []
t2.append(twoToTen(two))
t3.append(threeToTen(three))
for i in range(0, len(two)):
    if two[i] == "1":
        if i == 0:
            temp = "0" + two[1:]
        else:
            temp = two[0:i] + "0" +two[i+1:]
        t2.append(twoToTen(temp))
    else:
        if i == 0:
            temp = "1" + two[1:]
        else:
            temp = two[0:i] + "1" +two[i+1:]
        t2.append(twoToTen(temp))


for i in range(0, len(three)):
    if three[i] == "1":
        if i == 0:
            temp = "0" + three[1:]
            t3.append(threeToTen(temp))
            temp = "2" + three[1:]
            t3.append(threeToTen(temp))
        else:
            temp = three[0:i] + "0" +three[i+1:]
            t3.append(threeToTen(temp))
            temp = three[0:i] + "2" + three[i + 1:]
            t3.append(threeToTen(temp))
    elif three[i] == "2":
        if i == 0:
            temp = "0" + three[1:]
            t3.append(threeToTen(temp))
            temp = "1" + three[1:]
            t3.append(threeToTen(temp))
        else:
            temp = three[0:i] + "0" + three[i + 1:]
            t3.append(threeToTen(temp))
            temp = three[0:i] + "1" + three[i + 1:]
            t3.append(threeToTen(temp))
    else:
        if i == 0:
            temp = "2" + three[1:]
            t3.append(threeToTen(temp))
            temp = "1" + three[1:]
            t3.append(threeToTen(temp))
        else:
            temp = three[0:i] + "2" + three[i + 1:]
            t3.append(threeToTen(temp))
            temp = three[0:i] + "1" + three[i + 1:]
            t3.append(threeToTen(temp))

a = len(t2)
b = len(t3)
if a > b:
    for i in range(0, a):
        if t2[i] in t3:
            print(t2[i], end="")
else:
    if sorted(t2) == sorted(t3):
        print(2, end="")
    else:
        for i in range(0, b):
            if t3[i] in t2:
                print(t3[i], end="")