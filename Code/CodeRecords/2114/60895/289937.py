n=int(input())
times=0
stop=False
temp=[]
temp.append(n)
while stop==False:
    level=[]
    for item in temp:
        k=1
        while k*k<=item:
            k=k+1
        k=k-1        
        for i in range(1,k+1):
            level.append(item-i*i)
    times=times+1
    temp=[]
    for item in level:
        if item==0:
            stop=True
            break
        else:
            temp.append(item)
print(times)        