def devide(dividend,divisor):
    result=-1
    while dividend>=0:
        dividend-=divisor;
        result+=1
    return result
dividend=int(input())
divisor=int(input())
if dividend>0 and divisor >0:
    print(devide(dividend,divisor))
elif dividend > 0 and divisor<0:
    print(-(devide(dividend,-divisor)))
elif dividend < 0 and divisor > 0:
    print(-(devide(-dividend,divisor)))
elif dividend < 0 and divisor<0:
    print((devide(-dividend,-divisor)))