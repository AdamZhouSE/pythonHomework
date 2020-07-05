dividend=int(input())
divisor=int(input())
sign=False
if (dividend<0 and divisor>0) or(dividend>0 and divisor<0):
    sign=True
divisor=abs(divisor)
dividend=abs(dividend)
count=0
while (dividend>divisor):
    dividend-=divisor
    count+=1
if sign:
    print("-"+str(count))
else:
    print(count)