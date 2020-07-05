dividend=int(input())
divisor=int(input())
sign='+'
if (divisor>0 and dividend<0) or (divisor<0 and dividend>0):
    sign='-'
dividend=abs(dividend)
divisor=abs(divisor)
ans=0
while dividend>=divisor:
    ans+=1
    dividend-=divisor
if sign == '-':
    ans=-ans
print(ans)