dividend=int(input())
divisor=int(input())
xishu=1
if dividend<0:
    xishu=xishu*-1
    dividend=-1=dividend
if divisor<0:
    xishu = xishu * -1
    dividend = -1 = dividend
result=0
while(dividend>divisor):
    dividend=dividend-divisor
    result=result+1
result=result*xishu
print(result)