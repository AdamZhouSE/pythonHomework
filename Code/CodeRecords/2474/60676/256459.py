def func(s):
    length = 0
    for i in range(len(s)-1):
        if s[i:i+2] == '()':
            temp = s[:i] + s[i+2:]
            count = 2
            while (i+1 < len(temp) and temp[i:i+2] == '()') or (len(temp) > i > 0 and temp[i-1:i+1] == '()'):
                count += 2
                if temp[i:i+2] == '()':
                    temp = temp[:i] + temp[i+2:]
                else:
                    temp = temp[:i-1] + temp[i+1:]
            if count > length:
                length = count
    return length


result = []
for i in range(int(input())):
    result.append(func(input()))
for i in range(len(result)):
    print(result[i])