data = list(input())
if abs(data.count('a') - data.count('b')) >= 2:
    print("")
else:
    a = data.count('a')
    b = data.count('b')
    result = ''
    if a >= b:
        for i in range(a + b):
            if i % 2 == 0:
                result += 'a'
            else:
                result += 'b'
    else:
        for i in range(a + b):
            if i % 2 == 0:
                result += 'b'
            else:
                result += 'a'
    print(result)
