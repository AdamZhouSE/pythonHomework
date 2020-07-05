n=int(input())
def wow(j):
    for i in j:
        if not i:
            return False
    return True
def cha(heng,shu):
    if heng==1:
        return [0,1]
    elif heng==-1:
        return [0,-1]
    elif shu==-1:
        return[1,0]
    else:
        return[-1,0]
for q in range(n):
    x=input().split()
    hang=int(x[0])
    lie=int(x[1])
    x=input().split()
    
    a=[]
    for i in range(hang):
        tmp=[]
        for j in range(lie):
            tmp.append(x[i*lie+j])
        a.append(tmp)
    heng=1
    shu=0
    tmp=[False]*lie
    jud=[False]*hang*lie
    
    #print(a)
    #print(jud)
    res=[]
    i=-1
    j=0
    #print(wow(jud))
    while not wow(jud):
        i+=heng
        j+=shu   
        if i>=lie or i<0 or j>=hang or j<0 or jud[j*lie+i]==True:
            i-=heng
            j-=shu
            tmp=cha(heng,shu)
            heng=tmp[0]
            shu=tmp[1]
            #print(heng)
            #print(shu)
        else:
            jud[j*lie+i]=True
            res.append(a[j][i])
        #if hang*lie!=16 and len(res)>6:print(res)
        #print(wow(jud)) 
        if len(res)==hang*lie:break
    for i in res:
        print(i,end=" ")
    print()
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    










    