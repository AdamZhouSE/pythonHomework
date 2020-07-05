string = input()
result = 0
for i in range(len(string)):
    if string[i] == "I":
        result += 1
    elif string[i] == "V":
        if i > 0 and string[i-1] == "I":
            result += 3
        else:
            result += 5
    elif string[i] == "X":
        if i > 0 and string[i - 1] == "I":
            result += 8
        else:
            result += 10
    elif string[i] == "L":
        if i > 0 and string[i - 1] == "X":
            result += 30
        else:
            result += 50
    elif string[i] == "C":
        if i > 0 and string[i-1] == "X":
            result += 80
        else:
            result += 100
    elif string[i] == "D":
        if i > 0 and string[i-1] == "C":
            result += 300
        else:
            result += 500
    elif string[i] == "M":
        if i > 0 and string[i-1] == "C":
            result += 800
        else:
            result += 1000
print(result)

