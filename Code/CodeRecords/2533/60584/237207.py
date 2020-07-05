num = [int(n) for n in (input()[1:-1]).split(",")]
i = 0
j = len(num)-1
while(i<j):
    if(num[i]%2==0):
        i+=1
    
    elif(num[j]%2==1):
        j-=1
    
    else:
        temp=0
        temp=num[i]
        num[i]=num[j]
        num[j]=temp
        i+=1
        j-=1
print(num)