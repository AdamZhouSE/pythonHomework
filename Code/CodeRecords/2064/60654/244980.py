s = list(input())
result = 0
for i in range(s.__len__()):
    if s[i] == "I":
        if i != s.__len__()-1:
            if (s[i+1] == "V") | (s[i+1] == "X"):
                result += -1
            else:
                result += 1
        else:
            result += 1
    elif s[i] == "V":
        result += 5
    elif s[i] == "X":
        if i != s.__len__()-1:
            if (s[i+1] == "L") | (s[i+1] == "C"):
                result += -10
            else:
                result += 10
        else:
            result += 10
    elif s[i] == "L":
        result += 50
    elif s[i] == "C":
        if i != s.__len__()-1:
            if (s[i+1] == "D") | (s[i+1] == "M"):
                result += -100
            else:
                result += 100
        else:
            result += 100
    elif s[i] == "D":
        result += 500
    elif s[i] == "M":
        result += 1000
print(result)
