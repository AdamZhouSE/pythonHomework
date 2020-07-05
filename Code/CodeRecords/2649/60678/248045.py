def bin2int(string):
    outcome = 0
    for i in range(0,len(string)):
        bit = string[len(string) - i - 1]
        bit = int(bit)
        outcome = outcome + bit * 2 ** i
    return outcome


def int2bin(num):
    outcome = ''
    while num != 0:
        outcome = str(num % 2) + outcome
        num = num // 2
    return outcome


times = int(input())
for loopTimes in range(0, times):
    # 每个测试用例的循环
    userInput = input().split()
    numBin = int2bin(int(userInput[0]))
    numBin = list(numBin)
    numBin.reverse()
    for i in range(int(userInput[1]) - 1, int(userInput[2])):
        if numBin[i] == '0':
            numBin[i] = '1'
        elif numBin[i] == '1':
            numBin[i] = '0'
    numBin.reverse()
    print(bin2int(''.join(numBin)))