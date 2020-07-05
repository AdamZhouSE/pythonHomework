dividend=int(input())
if dividend<0:
    dd=dividend*(-1)
else:
    dd=dividend
divisor=int(input())
if divisor<0:
    dr=divisor*(-1)
else:
    dr=divisor               #默认divisor不为0

result=0
while dd>dr:
    dd=dd-dr
    result=result+1

if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0):
    result=result*(-1)
print(result)