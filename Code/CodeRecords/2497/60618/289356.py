n=int(input())
position=eval(input())
speed=eval(input())
car=len(position)
for k in range(0,n):
    
    for i in range(0,len(position)):
        if position[i]!=-1:
            position[i]=position[i]+speed[i]
            '''
        if position[i]>=n:
            position[i]=-1
            car+=1
            '''
    for i in range(0,len(position)-1):
        for j in range(i+1,len(position)):
            if position[i]==position[j] and position!=-1:
                car-=1
                position[j]=-1
                speed[i]==min(speed[i],speed[j])
                speed[j]=0
                if position[i]>=n:
                    position[i]=-1
                    speed[i]=0
print(car)                    
                
            