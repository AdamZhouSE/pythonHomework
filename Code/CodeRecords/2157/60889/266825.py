romanNum = input()
last = "A"
num = 0
for letter in romanNum:
    if letter == "I":
        num = num + 1
    elif letter == "V":
        num = num + 5
        if last == "I":
            num = num - 2
    elif letter == "X":
        num = num + 10
        if last == "I":
            num = num - 2
    elif letter == "L":
        num = num + 50
        if last == "X":
            num = num - 20
    elif letter == "C":
        num = num + 100
        if last == "X":
            num = num - 20
    elif letter == "D":
        num = num + 500
        if last == "C":
            num = num - 200
    elif letter == "M":
        num = num + 1000
        if last == "C":
            num = num - 200
    last = letter
print(num)