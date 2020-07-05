def romeNum(ch):
    if ch == 'I':
        return 1
    elif ch == 'V':
        return 5
    elif ch == 'X':
        return 10
    elif ch == 'L':
        return 50
    elif ch == 'C':
        return 100
    elif ch == 'D':
        return 500
    elif ch == 'M':
        return 1000

rome = input()
total = 0

for i in range(len(rome) - 1):
    trueNum = romeNum(rome[i])
    if trueNum < romeNum(rome[i + 1]):
        trueNum = -trueNum
    total += trueNum
total += romeNum(rome[len(rome) - 1])

print(total)