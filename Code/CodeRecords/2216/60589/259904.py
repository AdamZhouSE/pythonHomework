ans=eval(input())
if ans%1==0:
    print(str(int(ans))+'/'+'1')
else:
    d=2
    while (ans*d)%1!=0:
        d+=1
    u=int(ans*d)
    print(str(u)+'/'+str(d))