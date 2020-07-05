time=int(input())
while(time>0):
    len=int(input())
    str1=input()
    llist=str1.split()
    list=[]
    for c in llist:
        list.append(int(c))
        
    for i in range(len-1):
        if(list[i]!=0)and(list[i]==list[i+1]):
            list[i]*=2
            list[i+1]=0
    
    list2=[]
    for c in list:
        if(c!=0):
            list2.append(c)
            
    for c in list:
        if(c==0):
            list2.append(c)
            
            
    for x in range(len-1):
        print(str(list2[x])+" ",end="")
    print(list2[len-1])
    
    time-=1
    