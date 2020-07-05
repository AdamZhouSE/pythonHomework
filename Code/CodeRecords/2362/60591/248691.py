n = eval(input())
count = 0
result = ""
while(n != 0):
    count = count % 4
    if(count == 0):
        result += 'int('+str(n)
    else:
        result += str(n)

    if(count == 0):
        if(n != 1):
            result += '*'
        else:
            result += ')'
    elif(count == 1):
        if(n != 1):
            result += '/'
        else:
            result += ')'
    elif(count == 2):
        if(n != 1):
            result += ')+'
        else:
            result += ')'
    elif(count == 3):
        if(n != 1):
            result += '-'
    count += 1
    n = n - 1
print(eval(result))