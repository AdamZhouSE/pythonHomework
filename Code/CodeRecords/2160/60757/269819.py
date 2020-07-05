dividend=int(input())
divisor=int(input())
sign=0
if (dividend>0 and divisor<0)or(dividend<0 and divisor>0):
    sign=1
dividend=abs(dividend)
divisor=abs(divisor)
count=0
while(dividend>divisor):
    dividend=dividend-divisor
    count=count+1
if sign==1:
    count=-count
print(count)