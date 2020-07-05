t = int(input())
for ind in range(t):
    num = [ord(c) for c in input()]
    num.sort()
    num.reverse()
    maxL = 0
    startIndex = 0
    endIndex = 0
    for i in range(len(num)-1):
        diff = num[i+1] - num[i]
        j = i+2
        while j < len(num) and num[j]-num[j-1] == diff:
            j += 1
        if j - i > maxL:
            maxL = j - i
            startIndex = i
            endIndex = j
    result = []
    while startIndex < endIndex:
        result.append(chr(num[startIndex]))
        startIndex += 1
    print(''.join(result))