def dealRes():
    strs=input()
    n=int(strs.split(" ")[0])
    x0=int(strs.split(" ")[1])
    y0=int(strs.split(" ")[2])
    pos=[]
    res=0
    count=0
    while count<n:
        ssss=input()
        pos.append(ssss)
        count+=1
    while len(pos)>1:
        index=1
        tx=int(pos[0].split(" ")[0])
        ty=int(pos[0].split(" ")[1])
        if tx==x0:
            while index<len(pos):
                if int(pos[index].split(" ")[0])==x0:
                    pos.pop(index)
                else:
                    index+=1
        elif ty==y0:
            while index<len(pos):
                if int(pos[index].split(" ")[1])==y0:
                    pos.pop(index)
                else:
                    index+=1
        else:
            sx=(ty-y0)/(tx-x0)
            s=(y0*tx-x0*ty)/(tx-x0)
            while index<len(pos):
                if sx*int(pos[index].split(" ")[0])+s==int(pos[index].split(" ")[1]):
                    pos.pop(index)
                else:
                    index+=1
        res+=1
    
    print(res)
    
    
dealRes()
