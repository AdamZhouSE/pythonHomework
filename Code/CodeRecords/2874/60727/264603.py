def so(x,num):
    pflow=0
    eflow=0
    res=0
    for i in range(0,num):
        if x[i]==0:
            res+=1
            pflow,eflow=0,0
        elif x[i]==1:
            if pflow==1:
                res+=1
                pflow,eflow=0,0
            else:
                pflow=1
                eflow=0
        elif x[i]==2:
            if eflow==1:
                res+=1
                pflow,eflow=0,0
            else:
                eflow=1
                pflow=0
        else:
            if eflow==1 and pflow==1:
                res+=1
                eflow=0
                pflow=0
            elif eflow==1 and pflow==0:
                pflow=1
                eflow=0
            elif eflow==0 and pflow==1:
                eflow=1
                pflow=0
            else:
                if i+1<num-1:
                    if x[i+1]==0:
                        continue
                    elif x[i+1]==1:
                        eflow+=1
                        pflow=0
                    elif x[i+1]==2:
                        pflow+=1
                        eflow=0
                    else:
                        eflow=1
                        pflow=0
                else:
                    break
    return res
num = int(input())
x=input().split(' ')
x=list(map(int,x))
print(so(x,num))