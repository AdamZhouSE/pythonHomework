N=int(input())
res=0
for i in range(1,N+1):
    if(i%2==1):
        if(N%i==0):
            position=int(i/2)
            medium=int(N/i)
            if medium-position>0:
                res+=1
    else:
        if(N%i==int(i/2)):
            medium=int(N/i)
            position=int(i/2)-1
            if medium-position>0:
                res+=1
print(res)
            
            