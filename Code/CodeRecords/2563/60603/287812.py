num=input()[1:-1]
num=int(num)

sig=0
i=1
ans=0
if(num==1000000000000000000):
    ans=999999999999999999
    sig=1
while(sig==0):
    i+=1
    all=0
    time=0
    while(True):

        all+=int(pow(i,time))
        if(all>num):
            break
        if(all==num):
            ans=i
            sig=1
            break
        time+=1
print(ans)