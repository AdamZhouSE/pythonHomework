time=int(input())
listj=[2,4,8,16,32,64,128,256,512]
while(time>0):
    time-=1
    place=int(input())
    temp=0
    group=0
    for i in range(9):
        if(temp+listj[i]==place):
            group=i
            break
        if(temp+listj[i]>place):
            group=i
            break
        temp+=listj[i]
        
    cntingrp=place-temp-1
    weishu=group+1
    zuneishu=listj[group]
    finl=[]
    i=1
    cntingrp*=2
    while(weishu>0):
        weishu-=1
        cntingrp=int(cntingrp/2)
        if(cntingrp%2==0):
            finl.append(str(4))
        else:
            finl.append(str(7))
    finl.reverse()
    strr="".join(finl)
    print(strr)
    
    

            