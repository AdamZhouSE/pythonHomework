A=list(map(str,input()[2:-2].split('","')))
similars=[]
i=0
temp=[]
while(A):
    similars.append([A.pop(0)])
    for worda in A:
        s=0
        j=0
        k=0
        for wordb in similars[i]:
            for m in range(len(worda)):
                if(worda[m]!=wordb[m]):
                    j=m
                    k=k+1
            if(k==2):
                if(worda[j]==wordb[worda.index(wordb[j])] and wordb[j]==worda[wordb.index(worda[j])]):
                    similars[i].append(worda)
                    s=1
                    break
        if(s==0):
            temp.append(worda)
    A=temp[:]
    temp=[]
    i+=1
print(len(similars)-1)
    
            
        
