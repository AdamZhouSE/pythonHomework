dividend = int(input())
divisor = int(input())
quotient = 0
temp = dividend
if(dividend==0):
    print(0)
elif (dividend*divisor>0):
    if(dividend>0):
        while(temp>0):
            temp = temp-divisor
            quotient = quotient + 1
        if(temp<0):
            quotient -= 1
    else:
        while(temp<0):
            temp = temp - divisor
            quotient = quotient + 1
        if (temp > 0):
            quotient -= 1
else:
    if (dividend > 0):
        while (temp > 0):
            temp = temp + divisor
            quotient = quotient - 1
        if (temp < 0):
            quotient += 1
        else:
            while (temp < 0):
                temp = temp + divisor
                quotient = quotient - 1
            if (temp > 0):
                quotient += 1
print(quotient)