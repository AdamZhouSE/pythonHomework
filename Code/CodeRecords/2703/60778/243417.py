str=input()
M=eval(str)
size=len(M)
ctd=[0]*size
res=0
i=0
j=0
while(i<size):
    if(ctd[i]==0):
        j=i
        while(j<size):
            if(M[i][j]==1):
                ctd[j]=1
            j+=1
        res+=1
    i+=1
print(1)