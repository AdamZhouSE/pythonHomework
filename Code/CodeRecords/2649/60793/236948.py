testNum = int(input())
tests = []
for i in range(0, testNum):
    tests.append(list(map(int, input().split(" "))))
for test in tests:
    toConvert = test[0]
    start = test[1]
    end = test[2]
    strToConvert = str(bin(toConvert))[2:]
    convert = list(strToConvert)
    for i in range(start, end+1):
        if strToConvert[i] == '1':
            convert[i] = '0'
        else:
            convert[i] = '1'
    print(int("".join(convert), 2))