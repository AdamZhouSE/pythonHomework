dividend=int(input())
divisor=int(input())
negative1=False
negative2=False
if dividend<0:
    negative1=True
    dividend=-divedend
if divisor<0:
    negative2=True
    divisor=-divisor
rs=0
while dividend-divisor>=0:
    rs+=1
    dividend=dividend-divisor
if (negative1 and negative2)is False and(negative1 or negative2)is True:
    rs=-rs
print(rs)
