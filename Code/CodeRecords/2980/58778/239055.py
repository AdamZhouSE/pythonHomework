str=input()
order=input()
orderl=order.split( )
for i in range(len(orderl)):
    if orderl[i]=='D':
        x=str.find(orderl[i+1])
        if(x!=-1):
            str=str.replace(orderl[i+1],'',1)
        else:
            print('no exist')
    elif orderl[i]=='I':
        a1=orderl[i+1]
        a2=orderl[i+2]
        x=str.rfind(a1)
        if(x!=-1):
            str=str[:x]+a2+str[x:]
        else:
            print('no exist')
    elif orderl[i]=='R':
        
        a1=orderl[i+1]
        x=str.find(a1)
        a2=orderl[i+2]
        if(x!=-1):
            str=str.replace(a1,a2)
        else:
            print('no exist')
print(str)