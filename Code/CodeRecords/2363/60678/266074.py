def ten2bin(num):
    outcome = ''
    while num != 0:
        outcome = str(num % 2) + outcome
        num = num // 2
    return outcome


def bin2ten(binStr):
    outcome = 0
    for i in range(0, len(binStr)):
        if binStr[len(binStr) - i - 1] == '1':
            outcome += 2 ** i
    return outcome


num = int(input())
binStr = ten2bin(num)
binStr = binStr.replace('0', 'a').replace('1', '0').replace('a', '1')
print(bin2ten(binStr))