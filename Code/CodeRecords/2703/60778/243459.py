str=input()
M=eval(str)
size=len(M)
ctd=[0]*size
res=0
i,j,k=0
while(i<size):
    if(ctd[i]==0):
        j=i
        while(j<size):
            while(k<size):
                if(M[j][k]==1):
                    ctd[k]=1
                k+=1
            j+=1
        res+=1
    i+=1
print(res)