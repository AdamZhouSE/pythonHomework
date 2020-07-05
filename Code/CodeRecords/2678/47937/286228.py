n=int(input())

i=0
while i<n:
    temp=bin(int(input()))
    #print(temp)
    k=2
    one=0
    pos=0
    while k<len(temp):
        if(temp[k]=="1" and one==0):
            one=1
            pos=k
            #print("123123")
        elif(temp[k]=="1" and one==1):
            one=2
            break
        k=k+1
        
    if(one==2 or one==0):
        print(-1)
    else:
        print(pos)
        
            
    
    i=i+1