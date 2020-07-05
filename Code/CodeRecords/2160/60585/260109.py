dividend=eval(input())
divisor=eval(input())
res=0
if (dividend>=0)&(divisor>0):
    while dividend>=divisor:
        dividend-=divisor
        res+=1
elif (dividend<=0)&(divisor>0):
    dividend=-dividend
    while dividend>=divisor:
        dividend-=divisor
        res-=1
elif (dividend>=0)&(divisor<0):
    divisor=-divisor
    while dividend>=divisor:
        dividend-=divisor
        res-=1
else:
    divisor=-divisor
    dividend=-dividend
    while dividend>=divisor:
        dividend-=divisor
        res+=1
print(res)