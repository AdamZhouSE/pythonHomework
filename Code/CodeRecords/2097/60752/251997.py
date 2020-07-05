dividend=int(input())
divisor=int(input())
rs='%.10f'%(dividend/divisor)
r=str(float(rs))
if len(r)<len(rs):
    if int(r.split('.')[1])==0:
        print(r.split('.')[0])
    else:
        print(r)
else:
    rr=r.split('.')[1]
    found=False
    for len in range(1,6):
        for index in range(5):
            if rr[index:index+len]==rr[index+len:index+2*len]:
                if index>0:
                    print(r[0] + '.' +rr[0:index]+ '(' + rr[index:index + len] + ')')
                else:print(r[0]+'.'+'('+rr[index:index+len]+')')
                found=True
                break
        if found:break
