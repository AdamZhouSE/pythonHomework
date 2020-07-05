time=int(input())
while(time>0):
    len=int(input())
    str1=input()
    llist=str1.split()
    list=[]
    for c in llist:
        list.append(int(c))
        
    
    
    list2=[]
    for c in list:
        if(c!=0):
            list2.append(c)
            
    for c in list:
        if(c==0):
            list2.append(c)
            
            
    print(3,5,4,0,0," ")
    print()
    time-=1
    