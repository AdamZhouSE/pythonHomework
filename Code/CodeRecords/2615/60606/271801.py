test_num = int(input())
result = []
for i in range(test_num):
    s = input()
    gap = ord(s[0]) - ord(s[1])
    temp = s[0:2]
    for j in range(1,len(s)-1):
        if ord(s[j]) - ord(s[j+1]) == gap:
            temp += s[j+1]
        else:
            if len(temp) >= 3:
                result.append(temp)
                temp = s[j+1]
            if  j < len(s) -2:
                gap = ord(s[j+1]) - ord(s[j+2])
            else:
                break
    if result.count(temp) == 0:
        result.append(temp)
    result2 = []
    maxLength = 0
    for item in result:
        if len(item) > maxLength:
            maxLength = len(item)
    for item in result:
        if len(item) == maxLength:
            result2.append(item)
    result2.sort()
    output = list(result2[-1])
    output.reverse()
    print("".join(output))


