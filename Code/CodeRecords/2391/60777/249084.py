n=int(input())
name=[]

for i in range(n):
    name.append(input())
    
m=int(input())
count=[0]*n

for i in range(m):
    call=input()
    find=False
    for j in range(n):
        if(name[j]==call and count[j]==0):
            print("OK")
            count[j]=1
            find=True
            break
        elif(name[j]==call and count[j]!=0):
            print("REPEAT")
            find=True
            break
    if(find==False):
        print("WRONG")
        
            
        