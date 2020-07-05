ts=int(input())
cs=int(input())

list1=[]

if ts>0 and cs>0:
    for i in range(1,cs+1):
        if (ts-4*i) == (2*(cs-i)):
            list1.append(i)
            list1.append(cs-i)
            
elif ts==cs and ts==0:
    list1.append(0)
    list1.append(0)
    
if ts==2 and cs==1:  
    list1.append(0)
    list1.append(1)
    
print(list1)