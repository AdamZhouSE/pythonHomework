def get(a):
    sport=0
    program=0
    if a==0:
        return sport,program
    elif a==1:
        program=1
        return sport,program
    elif a==2:
        sport=1
        return sport,program
    else:
        sport=1
        program=1
        return sport,program
n=int(input())
day=list(map(int,input().split()))
y_s=0
y_p=0
both=0
rest=0
for i in range(n):
    s,p=get(day[i])
    if(s==0 and p==0):
        both=1
        rest+=1
    elif(s==0 and p==1):
        if both==1:
            y_p=1
            y_s=0
            both=0
        elif(y_p==1):
            y_p=0
            y_s=0
            both=1
            rest+=1
        elif(y_p==0):
            y_p=1
            y_s=0
            both=0
    elif(s==1 and p==0):
        if both==1:
            y_p=0
            y_s=1
            both=0
        elif(y_s==1):
            y_p=0
            y_s=0
            both=1
            rest+=1
        elif(y_s==0):
            y_p=0
            y_s=1
            both=0
    else:
        if both==1:
            both=1
        elif(y_p==1):
            y_s=1
            y_p=0
            both=0
        elif(y_s==1):
            y_p=1
            y_s=0
            both=0
print(rest)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        