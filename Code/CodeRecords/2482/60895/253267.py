t=int(input())
while t>0:
    n=int(input())
    d=int(input())
    t=t-1
    result=''
    if n%d==0:
        result=str(n//d)
    else:
        num=float(n/d)
        result=str(num)
        start=result[0:2]
        dec=result[2:]
        index=1
        for i in range(0,len(dec)-2):
            if dec[i]==dec[i+1]:
                index=index+1
        if index==len(dec)-1:
            dec='('+dec[0]+')'
        result=start+dec
    print(result)