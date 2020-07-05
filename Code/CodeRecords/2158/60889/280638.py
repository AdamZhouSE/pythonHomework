def atoi(string):
    string = string.strip(" ")
    if not (string[0].isdigit() or  string[0]=="-"):
        return 0
    isNeg = False
    if string[0] == "-":
        isNeg = True
        string = string.strip("-")
    for i in range(len(string)):
        if not string[i].isdigit():
            break
    else:
        i = i + 1
    numStr = string[0:i]
    if len(numStr) < 10 or (len(numStr)==10 and int(numStr[0]) <2):
        num = int(numStr)
        if isNeg:
            num = - num
        return num
    elif len(numStr) > 10 or (len(numStr)==10 and int(numStr[0]) > 2):
        if isNeg:
            return -2**31
        else:
            return 2**30-1+2**30
    else:
        odd = numStr[1:]
        odd = int(odd)
        if isNeg:
            if odd > 147483648:
                return -2147483648
            else:
                return - odd -2000000000
        else:
            if odd > 147483647:
                return 2147483647
            else:
                return odd + 200000000
            
string = input()
print(atoi(string))