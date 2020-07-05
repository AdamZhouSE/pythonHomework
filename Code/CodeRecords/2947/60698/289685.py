def test():
    n = int(input())
    origin=input()
    operations=[]
    for _ in range(0,n):
        operations.append(input())
    for operation in operations:
        origin=oper(operation,origin)

def oper(operation,origin):
    operator=int(operation[0])
    operand=operation[2:]
    if operator==1:
        print(origin+operand)
        return origin+operand
    elif operator==2:
        operande=operand.split()
        begin=int(operande[0])
        num=int(operande[1])
        print(origin[begin:begin+num])
        return origin[begin:begin+num]
    elif operator==3:
        operande = operand.split()
        begin = int(operande[0])
        string = operande[1]
        origin=origin[0:begin]+string+origin[begin:]
        print(origin)
        return origin
    elif operator==4:
        if operand not in origin:
            print(-1)
            return origin
        else:
            for i in range(0,len(origin)):
                try:
                    if origin[i:i+len(operand)]==operand:
                        print(i)
                        return origin
                except:
                    print(-1)
                    return origin

test()