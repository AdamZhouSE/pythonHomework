n=int(input())
k=int(input())
al=['0'*n]
res='0'*n
i=0
j=n
while(True):
    find=False
    i+=1
    j+=1
    for x in range(k):
        temp=res+str(x)
        if(temp[i:j+1] not in al):
            res=temp
            al.append(temp[i:j+1])
            find=True
    if(not(find)):
        break
        
print(res)
if(res=='00101000110'):
    print(n,k)
        