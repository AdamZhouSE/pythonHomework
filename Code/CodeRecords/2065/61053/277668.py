def isdigit(ch):
    if ch >= '0' and ch <= '9':
        return True
    return False

def atoi(str):
    if len(str) == 0:
        return 0
    index = 0
    while index < len(str) and str[index] == ' ':
        index += 1
    if index == len(str):
        return 0

    if str[index] != '-' and not isdigit(str[index]):
        return 0

    isneg = False
    if str[index] == '-':
        isneg = True
        index += 1
    val = 0
    while index < len(str) and isdigit(str[index]):
        val *= 10
        val += int(str[index])
        index += 1

    if isneg:
        val *= -1

    if val > 2**31-1:
        val = 2**31-1
    if val < -2**31:
        val = -2**31
    return val

if __name__ == "__main__":
    str = input()
    print(atoi(str))