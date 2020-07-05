def operate(operation,str):
    wh=int(operation.split(" ")[0])
    if wh==1:
        _str=operation.split(" ")[1]
        str = str + _str
        print(str)
        return str
    if wh==2:
        a=int(operation.split(" ")[1])
        b=int(operation.split(" ")[2])
        sum=a+b
        if sum>len(str):
            sum=-1
        str = str[a:sum]
        print(str)
        return str
    if wh==3:
        a=int(operation.split(" ")[1])
        _str=operation.split(" ")[2]
        str = str[0:a] + _str + str[a:]
        print(str)
        return str
    if wh==4:
        _str=operation.split(" ")[1]
        if (len(_str) > len(str)):
            print(-1)
        eq = -1
        for i in range(len(str) - len(_str) + 1):
            if str[i:i + len(_str)] == _str:
                eq = i
                break
        print(eq)
        return str
    return -1
num=input()
str=input()
for i in range(int(num)):
    str=operate(input(),str)
