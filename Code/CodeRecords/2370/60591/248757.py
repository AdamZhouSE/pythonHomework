n = eval(input())
result = []
if(n == 1):
    print(1)
else:
    while(n != 0):
        if(n % 2 == 1):
            result.append(1)
        else:
            result.append(0)
        if(n == -1):
            result.append(1)
        n = int(n / -2)
    result.reverse()
    result = list(map(str,result))
    print("".join(result))