time=int(input())
result=[]
while time>0:
    dividend=int(input())
    divisor=int(input())
    time=time-1
    integar,decimal=map(str,str(dividend/divisor).split('.'))

    dec=''
    if len(decimal)==16:
        for item in decimal[:15]:
            if item not in dec:
                dec=dec+item
        dec='.('+dec+')'
    elif decimal=='0':
        dec=''
    else:
        dec='.'+decimal
    res=integar+dec
    result.append(res)
for res in result:
    print(res)