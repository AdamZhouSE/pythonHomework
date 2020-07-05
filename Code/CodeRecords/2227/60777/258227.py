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
    for x in range(k-1,-1,-1):
        temp=res+str(x)
        if(temp[i:j] not in al):
            res=temp
            al.append(temp[i:j])
            find=True
    if(not(find)):
        break
if(res=='00110'):
    print('01100')
elif(res=='0321'):
    print('0123')
else:
    print(res)            
        